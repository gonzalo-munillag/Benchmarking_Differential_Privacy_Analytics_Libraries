package examples

import java.io.{FileWriter, PrintWriter}
import chorus.schema.Schema
import chorus.sql.QueryParser
import chorus.mechanisms.LaplaceMechClipping
import chorus.mechanisms.AverageMechClipping
import chorus.mechanisms.EpsilonCompositionAccountant
import chorus.rewriting.RewriterConfig

import scala.collection.mutable
import scala.io.Source.fromFile


object EvaluationDriver extends App {

  val dataset_num = "dataset_0"

  def StandardDeviation[A](a: Seq[A])(implicit num: Numeric[A]):Double = {

    def mean(a: Seq[A]): Double = num.toDouble(a.sum) / a.size

    def variance(a: Seq[A]): Double = {
      val avg = mean(a)
      a.map(num.toDouble).map(x => math.pow((x - avg),2)).sum / a.size
    }

    math.sqrt(variance(a))

  }

  def getMax(list: mutable.MutableList[Double]): Double = {
    var max = list.head
    for (item <- list) {
      if (item > max)
        max = item
    }
    max
  }

  def getMin(list: mutable.MutableList[Double]): Double = {
    var min = list.head
    for (item <- list) {
      if (item < min)
        min = item
    }
    min
  }

  //val dataset_num = "dataset_0"

  val results: mutable.MutableList[Double] = mutable.MutableList()
  val lines = fromFile("normal_distribution_datasets//" + dataset_num + ".csv").getLines
  for (line <- lines) {
    if(!line.equals("field1")) {
      results.+=(line.toDouble)
    }
  }




  def meanElements(list: Seq[Double]): Double = list.sum / list.length

  System.setProperty("dp.elastic_sensitivity.check_bins_for_release", "false")
  System.setProperty("db.use_dummy_database", "true")

  val EPS_list = Array(0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0) // privacy parameter

  // Use the table schemas and metadata defined by the test classes
  System.setProperty("schema.config.path", "src/test/resources/schema_eval.yaml")
  val database = Schema.getDatabase("test")
  val config = new RewriterConfig(database)

  // Define the privacy accountant
  val accountant = new EpsilonCompositionAccountant()

  val true_count = results.size
  val true_sum = results.sum
  val true_avg = meanElements(results)

  for (EPSILON <- EPS_list){
  println("Calculating results for epsilon = " + EPSILON)

  var relative_err_count: mutable.MutableList[Double] = mutable.MutableList()
  var scale_err_count: mutable.MutableList[Double] = mutable.MutableList()

  var relative_err_sum: mutable.MutableList[Double] = mutable.MutableList()
  var scale_err_sum: mutable.MutableList[Double] = mutable.MutableList()

  var relative_err_avg: mutable.MutableList[Double] = mutable.MutableList()
  var scale_err_avg: mutable.MutableList[Double] = mutable.MutableList()


  // Run a COUNT query **************************************************
  val t1 = System.nanoTime // execution time start
  val countQuery = "SELECT COUNT(*) FROM " + dataset_num
  val countRoot = QueryParser.parseToRelTree(countQuery, database)

    val lCount = new LaplaceMechClipping(EPSILON, getMin(results), getMax(results), countRoot, config)
    //val true_count = results.size
    val countResults = (1 to 500) map {
      x => lCount.execute(accountant).head.vals.head.toDouble   // run it 500 times
    }
    val duration = (System.nanoTime - t1) / 1e9d  //execution time end
    println("COUNT Execution Time: " + duration)
    println("COUNT query mean: " + meanElements(countResults))
 
    for (dp_count <- countResults){
    relative_err_count.+= (((true_count - dp_count)/true_count).abs)
    scale_err_count.+= (((true_count - dp_count)/true_count).abs)
    }
    println("COUNT query mean relative error: " + meanElements(relative_err_count))
    val guestFile1 = new PrintWriter(new FileWriter("results//chorus//count//results_" + dataset_num + "//mean_relative_error//DP_mean_relative_error.csv", true))
    guestFile1.println(meanElements(relative_err_count))
    guestFile1.close()

    println("COUNT query Std scaled error: " + StandardDeviation(scale_err_count))
    val guestFile2 = new PrintWriter(new FileWriter("results//chorus//count//results_" + dataset_num + "//std_scaled_error//DP_std_scaled_error.csv", true))
    guestFile2.println(StandardDeviation(scale_err_count))
    guestFile2.close()


    // Run a SUM query **************************************************
    val sumQuery = "SELECT SUM(field1) FROM " + dataset_num
    val sumRoot = QueryParser.parseToRelTree(sumQuery, database)

    val lSum = new LaplaceMechClipping(EPSILON, getMin(results), getMax(results), sumRoot, config)
    val sumResults = (1 to 500) map {
      x => lSum.execute(accountant).head.vals.head.toDouble   // run it 500 times
    }

    for (dp_sum <- sumResults){
    relative_err_sum.+= (((dp_sum - true_sum)/true_sum).abs)
    scale_err_sum.+= (((dp_sum - true_sum)/true_count).abs)
    }
    println("SUM query mean: " + meanElements(sumResults))
    println("SUM query mean relative error: " + meanElements(relative_err_sum))
    println("SUM query Std scaled error: " + StandardDeviation(scale_err_sum))

    val guestFile3 = new PrintWriter(new FileWriter("results//chorus//sum//results_" + dataset_num + "//mean_relative_error//DP_mean_relative_error.csv", true))    
    guestFile3.println(meanElements(relative_err_sum))
    guestFile3.close()

    val guestFile4 = new PrintWriter(new FileWriter("results//chorus//sum//results_" + dataset_num + "//std_scaled_error//DP_std_scaled_error.csv", true))   
    guestFile4.println(StandardDeviation(scale_err_sum)) 
    guestFile4.close()


    // Run a AVG query **************************************************
    val avgQuery = "SELECT AVG(field1) FROM " + dataset_num
    val avgRoot = QueryParser.parseToRelTree(avgQuery, database)

    val lAvg = new AverageMechClipping(EPSILON, getMin(results), getMax(results), avgRoot, config)
    val avgResults = (1 to 500) map {
      x => lAvg.execute(accountant).head.vals.head.toDouble   // run it 500 times
    }

    for (dp_avg <- avgResults){
    relative_err_avg.+= (((dp_avg - true_avg)/true_avg).abs)
    scale_err_avg.+= (((dp_avg - true_avg)/true_count).abs)
    }
    println("True AVG: " + true_avg)
    println("AVG query mean: " + meanElements(avgResults))
    println("AVG query mean relative error: " + meanElements(relative_err_avg)) 
    println("AVG query Std scaled error: " + StandardDeviation(scale_err_avg))

    val guestFile5 = new PrintWriter(new FileWriter("results//chorus//mean//results_" + dataset_num + "//mean_relative_error//DP_mean_relative_error.csv", true))
    guestFile5.println(meanElements(relative_err_avg))                                                                  
    guestFile5.close()
                                                                                                                             
    val guestFile6 = new PrintWriter(new FileWriter("results//chorus//mean//results_" + dataset_num + "//std_scaled_error//DP_std_scaled_error.csv",true))
    guestFile6.println(StandardDeviation(scale_err_avg))
    guestFile6.close()

  }
}
