#!/usr/bin/env bash

ATT=${1:-"WARC-Record-ID"}
INFILE=${2:-"hdfs:///user/bbkruit/CommonCrawl-sample.warc.gz"}
OUTFILE="temp"

PYSPARK_PYTHON=$(readlink -f $(which python)) ~/spark-2.1.2-bin-without-hadoop/bin/spark-submit \
--master yarn starter-code.py $ATT $INFILE $OUTFILE

hdfs dfs -cat $OUTFILE"/*"
