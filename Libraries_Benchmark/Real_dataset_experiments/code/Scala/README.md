# Running the Evaluation Code

Step 1: Clone the original repo (`git clone https://github.com/uber-archive/sql-differential-privacy`)  
Step 2: The driver to run the evaluation is in `src/main/scala/examples/EvaluationDriver.scala` - replace this file with our file  
Step 3: The schema is in `test/resources/schema_eval.yaml`  - replace this file with our file  
Step 4: The database is a SQLite3 database in `test_db.db` - put data in this database to change what gets evaluated when you run the experiment (recommended sqlite)    
Step 5: To build the code, use `mvn compile`  
Step 6: To run the experiment, use `mvn exec:java  -Dexec.mainClass="examples.EvaluationDriver"`

** in `src/main/scala/examples/EvaluationDriver.scala` you have to update:
	  Line 48: val dataset_num = "grade_education"  %% update it manually for each attribute (age_adult, hrs_adult, absences_adult, grade_adult)
  	  Line 49: val upr = 20 			%% age_adult=100, hrs_adult=80, absences_adult=93, grade_adult=20
  	  Line 50: val lwr = 0
  	  Line 51: val result_dataset = 4		%%age_adult=1, hrs_adult=2, absences_adult=3, grade_adult=4

** You also have to make cahnges in `test/resources/schema_eval.yaml` accordingly.
