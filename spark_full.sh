#!/usr/bin/env bash

# Usage: bash spark_full.sh [INFILE] [OUTFILE]
SCRIPT=${1:-"starter-code-spark.py"}
INFILE=${2:-"hdfs:///user/bbkruit/full.warc.gz"}
OUTFILE=${3:-"full"}

PYSPARK_PYTHON=$(readlink -f $(which python)) ~/spark-2.1.2-bin-without-hadoop/bin/spark-submit \
--master yarn $SCRIPT $INFILE $OUTFILE

hdfs dfs -cat $OUTFILE"/*" > $OUTFILE
