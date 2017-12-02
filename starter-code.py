from pyspark import SparkContext
import sys
import collections

sc = SparkContext("yarn", "wdps17XX")

record_attribute = sys.argv[1]
in_file = sys.argv[2]
out_file = sys.argv[3]

rdd = sc.newAPIHadoopFile(in_file,
    "org.apache.hadoop.mapreduce.lib.input.TextInputFormat",
    "org.apache.hadoop.io.LongWritable",
    "org.apache.hadoop.io.Text",
    conf={"textinputformat.record.delimiter": "WARC/1.0"})

def find_google(record):
    # finds google
    _, payload = record
    key = None
    for line in payload.splitlines():
        if line.startswith(record_attribute):
            key = line.split(': ')[1]
            break
    if key and ('Google' in payload):
        yield key + '\t' + 'Google' + '\t' + '/m/045c7b'

rdd = rdd.flatMap(find_google)

rdd = rdd.saveAsTextFile(out_file)
