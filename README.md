# wdps2017
Web Data Processing Systems 2017 (VU course XM_40020)

See also: http://bennokr.github.io/wdps2017

# Assignment 1: Large Scale Entity Linking
The first assignment for this course is to perform [Entity Linking](https://en.wikipedia.org/wiki/Entity_linking) on a collection of web pages. Your solution should be scalable and accurate, and conform to the specifications below. You should work in groups of 3 or 4 people, and use a version control system that we can access. After forming a group, set up a private version control repository using [BitBucket](https://bitbucket.org) or [Github](http://github.com) and give me access (my username is bennokr on both websites). If you need help with this, contact me. You can use any existing languages or tools you want, as long as it's easy for us to run it on the DAS-4 cluster. Of course, your solution is not allowed to call web services over the internet. You are encouraged to use the technologies covered in the lectures.

Your solution should be runnable trough a bash script with the command line options specified below. An example of some dummy starter code is available in this repository.

The input data is a gzipped [WARC file](https://en.wikipedia.org/wiki/Web_ARChive), and the ouput is a three-column tab-separated file with document IDs, entity surface forms (like "Berlin"), and Freebase entity IDs (like "/m/03hrz"). There is a sample file of the input (warc) and output (tsv) formats in this directory. Your program must accept two command line arguments: the WARC key name that is used in the web archive for identifying documents (like "WARC-Record-ID"), the HDFS path of the input and the HDFS path of the output. Your program must be runnable on the DAS4 cluster using a bash script, and you should provide a README file with a description of your approach. For example, your program could be run using the command `bash run.sh "WARC-Record-ID" "hdfs://user/yourname/input.warc.gz" > output.tsv`.

