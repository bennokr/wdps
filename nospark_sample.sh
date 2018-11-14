
time python3 starter-code.py <(hdfs dfs -cat hdfs:///user/bbkruit/sample.warc.gz | zcat) > sample_predictions.tsv

python3 score.py data/sample.annotations.tsv sample_predictions.tsv