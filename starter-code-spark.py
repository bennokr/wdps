from pyspark import SparkContext
import sys
import collections

sc = SparkContext("yarn", "wdps17XX")

KEYNAME = "WARC-TREC-ID"
INFILE = sys.argv[1]
OUTFILE = sys.argv[2]

rdd = sc.newAPIHadoopFile(INFILE,
    "org.apache.hadoop.mapreduce.lib.input.TextInputFormat",
    "org.apache.hadoop.io.LongWritable",
    "org.apache.hadoop.io.Text",
    conf={"textinputformat.record.delimiter": "WARC/1.0"})

def find_google(record):
    # finds google
    _, payload = record
    key = None
    for line in payload.splitlines():
        if line.startswith(KEYNAME):
            key = line.split(': ')[1]
            break
    if key and ('Google' in payload):
        yield key + '\t' + 'Google' + '\t' + '/m/045c7b'

rdd = rdd.flatMap(find_google)

rdd = rdd.saveAsTextFile(OUTFILE)
