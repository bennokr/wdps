#!/usr/bin/env bash

ATT=${1:-"WARC-Record-ID"}
INFILE=${2:-"hdfs:///user/bbkruit/CommonCrawl-sample.warc.gz"}

~/spark-2.2.0-bin-without-hadoop/bin/spark-submit --master yarn starter-code.py $ATT $INFILE
