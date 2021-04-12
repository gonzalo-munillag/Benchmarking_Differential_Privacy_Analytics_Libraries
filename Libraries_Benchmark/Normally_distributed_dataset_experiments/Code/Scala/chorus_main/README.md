# Running the Evaluation Code

- The driver to run the evaluation is in
  `examples/EvaluationDriver.scala` - modify this file to design the
  experiment itself
- The schema is in `test/resources/schema_eval.yaml`
- The database is a SQLite3 database in `test_db.db` - put data in
  this database to change what gets evaluated when you run the
  experiment
- To build the code, use `mvn compile`
- To run the experiment, use `mvn exec:java -Dexec.mainClass="examples.EvaluationDriver"`

# Overview

This repository contains the updated implementation of the Chorus
system for differential privacy, to accompany the following paper:

- **CHORUS: a Programming Framework for Building Scalable Differential
Privacy Mechanisms.** Noah Johnson, Joseph P. Near, Joseph
M. Hellerstein, Dawn Song. *EuroS&P 2020*.

This is an updated release of Chorus.  The original release of Chorus
is available
[here](https://github.com/uber-archive/sql-differential-privacy); see
the original repository and the paper for more documentation.

## Building & Running

This framework is written in Scala and built using Maven. The code has been tested on Mac OS X and Linux. To build the code:

```
$ mvn package
```

## Running Examples

The file `examples/MechanismExamples.scala` contains several examples
from the paper. To run the examples, after building Chorus:

```
mvn exec:java -Dexec.mainClass="examples.MechanismExamples"
```

## License

This project is released under the MIT License.

## Contact Information

This code is maintained by [Joe Near](http://www.uvm.edu/~jnear/).
