#!/usr/bin/env bash

ATT=${1:-"WARC-Record-ID"}
INFILE=${2:-"hdfs:///user/bbkruit/CommonCrawl-sample.warc.gz"}
OUTFILE="temp"

# This assumes there is a python virtual environment in the "venv" directory
source venv/bin/activate
virtualenv --relocatable venv
zip -r venv.zip venv

PYSPARK_PYTHON=$(readlink -f $(which python)) ~/spark-2.1.2-bin-without-hadoop/bin/spark-submit \
--conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/venv/bin/python \
--master yarn-cluster \
--archives venv.zip#VENV \
starter-code.py $ATT $INFILE $OUTFILE

hdfs dfs -cat $OUTFILE"/*"
