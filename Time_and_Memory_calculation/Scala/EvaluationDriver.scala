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

  val dataset_num = "dataset_6"

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

  val EPS_list = Array(0.1, 1.0, 10.0) // privacy parameter

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

  var m1: mutable.MutableList[Double] = mutable.MutableList()  
  var m2: mutable.MutableList[Double] = mutable.MutableList()
  var m3: mutable.MutableList[Double] = mutable.MutableList()
  
  var time1: mutable.MutableList[Double] = mutable.MutableList()
  var time2: mutable.MutableList[Double] = mutable.MutableList()
  var time3: mutable.MutableList[Double] = mutable.MutableList()
  
  // Run a COUNT query **************************************************
  for (i <- 1 to 100){

    val runtime1 = Runtime.getRuntime  // start memory consumtion calculation (ref: https://alvinalexander.com/scala/how-show-memory-ram-use-scala-application-used-free-total-max/)
    val t1 = System.nanoTime  // start time execution calculation
    // QUERY START
    val countQuery = "SELECT COUNT(*) FROM " + dataset_num
    val countRoot = QueryParser.parseToRelTree(countQuery, database)
    val lCount = new LaplaceMechClipping(EPSILON, getMin(results), getMax(results), countRoot, config)
    //val true_count = results.size
    val countResults = (1 to 2) map {
      x => lCount.execute(accountant).head.vals.head.toDouble   // run it 100 times
    }
    // QUERY END
    m1.+= ((runtime1.totalMemory - runtime1.freeMemory)/2)
    time1.+=(((System.nanoTime - t1) / 1e9d)/2)
  }
    //println("COUNT memory list length:  " + (m1))
    println("COUNT Used Memory:  " + meanElements(m1))
    val guestFile10 = new PrintWriter(new FileWriter("results//chorus//count//results_" + dataset_num + "//AVG_memory.csv", true))
    guestFile10.println(meanElements(m1))
    guestFile10.close()

    //val duration = ((System.nanoTime - t1) / 1e9d)/2  // end time execution calculation
    println("COUNT execution time: " + meanElements(time1))
    val guestFile7 = new PrintWriter(new FileWriter("results//chorus//count//results_" + dataset_num + "//execution_time.csv", true))
    guestFile7.println(meanElements(time1))
    guestFile7.close()

    /*
    //println("COUNT query mean: " + meanElements(countResults))
 
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
    */


    // Run a SUM query **************************************************
    for (j <- 1 to 100){

    val runtime2 = Runtime.getRuntime  // start memory consumtion calculation
    val t2 = System.nanoTime
    val sumQuery = "SELECT SUM(field1) FROM " + dataset_num
    val sumRoot = QueryParser.parseToRelTree(sumQuery, database)

    val lSum = new LaplaceMechClipping(EPSILON, getMin(results), getMax(results), sumRoot, config)
    val sumResults = (1 to 2) map {
      x => lSum.execute(accountant).head.vals.head.toDouble   // run it 2 times
    }
    m2.+=((runtime2.totalMemory - runtime2.freeMemory)/2)
    time2.+= (((System.nanoTime - t2) / 1e9d)/2)
    }

    println("SUM Used Memory:  " + meanElements(m2))
    val guestFile11 = new PrintWriter(new FileWriter("results//chorus//sum//results_" + dataset_num + "//AVG_memory.csv", true))
    guestFile11.println(meanElements(m2))
    guestFile11.close()
                         
    //val duration2 = ((System.nanoTime - t2) / 1e9d)/100  // end time execution calculation
    println("SUM execution time: " + meanElements(time2))      
    val guestFile8 = new PrintWriter(new FileWriter("results//chorus//sum//results_" + dataset_num + "//execution_time.csv", true))
    guestFile8.println(meanElements(time2))                                                                                                                          
    guestFile8.close()

    /*
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
    */


    // Run a AVG query **************************************************
    for (k <- 1 to 100) {
    val runtime3 = Runtime.getRuntime  // start memory consumtion calculation
    val t3 = System.nanoTime
    val avgQuery = "SELECT AVG(field1) FROM " + dataset_num
    val avgRoot = QueryParser.parseToRelTree(avgQuery, database)

    val lAvg = new AverageMechClipping(EPSILON, getMin(results), getMax(results), avgRoot, config)
    val avgResults = (1 to 2) map {
      x => lAvg.execute(accountant).head.vals.head.toDouble   // run it 2 times
    }
    m3.+= ((runtime3.totalMemory - runtime3.freeMemory)/2) 
    time3.+=(((System.nanoTime - t3) / 1e9d)/2)

    }
    println("MEAN Used Memory:  " + meanElements(m3))                                                                                         
    val guestFile12 = new PrintWriter(new FileWriter("results//chorus//mean//results_" + dataset_num + "//AVG_memory.csv", true))          
    guestFile12.println(meanElements(m3))  
    guestFile12.close()

    
    //val duration3 = ((System.nanoTime - t3) / 1e9d)/100  // end time execution calculation
    println("MEAN execution time: " + meanElements(time3))                                                           
    val guestFile9 = new PrintWriter(new FileWriter("results//chorus//mean//results_" + dataset_num + "//execution_time.csv", true)) 
    guestFile9.println(meanElements(time3))  
    guestFile9.close()

    /*
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
    */

  }
}
