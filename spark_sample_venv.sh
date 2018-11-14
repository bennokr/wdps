#!/usr/bin/env bash

# Usage: bash spark_venv.sh [INFILE] [OUTFILE]
SCRIPT=${1:-"starter-code-spark.py"}
INFILE=${2:-"hdfs:///user/bbkruit/sample.warc.gz"}
OUTFILE=${3:-"sample"}

# This assumes there is a python virtual environment in the "venv" directory
source venv/bin/activate
virtualenv --relocatable venv
zip -r venv.zip venv

PYSPARK_PYTHON=$(readlink -f $(which python)) ~/scratch/spark-2.1.2-bin-without-hadoop/bin/spark-submit \
--conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/venv/bin/python \
--master yarn-cluster \
--archives venv.zip#VENV \
$SCRIPT $INFILE $OUTFILE

hdfs dfs -cat $OUTFILE"/*" > $OUTFILE
