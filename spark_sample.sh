#!/usr/bin/env bash

# Usage: bash spark_sample.sh [INFILE] [OUTFILE]
SCRIPT=${1:-"starter-code-spark.py"}
INFILE=${2:-"hdfs:///user/bbkruit/sample.warc.gz"}
OUTFILE=${3:-"sample"}

PYSPARK_PYTHON=$(readlink -f $(which python)) ~/spark-2.1.2-bin-without-hadoop/bin/spark-submit \
--master yarn $SCRIPT $INFILE $OUTFILE

hdfs dfs -cat $OUTFILE"/*" > $OUTFILE
