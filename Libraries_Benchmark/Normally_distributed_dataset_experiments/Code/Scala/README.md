# (Scala) Differential privacy libraries benchmarked on sythetic datasets

EvaluationDriver.scala

- Line 52: update dataset file location.

### Running the Evaluation Code

Step 1: Clone the original repo (`git clone https://github.com/uber-archive/sql-differential-privacy`)

Step 2: The driver to run the evaluation is in  `src/main/scala/examples/EvaluationDriver.scala` - replace this file with our file

Step 3: The schema is in `test/resources/schema_eval.yaml`  - replace this file with our file

Step 4: The database is a SQLite3 database in `test_db.db` - put data in this database to change what gets evaluated when you run the experiment (recommended `sqlite')

Step 5: To build the code, use `mvn compile`

Step 6: To run the experiment, use `mvn exec:java -Dexec.mainClass="examples.EvaluationDriver"`

(for each dataset, change the dataset number in 
	`test/resources/schema_eval.yaml (Line: 7)` and 
	`src/main/scala/examples/EvaluationDriver.scala (Line: 17)` manually and then compile)
