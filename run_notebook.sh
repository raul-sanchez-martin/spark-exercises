#!/bin/bash

docker run -it -p 8888:8888 -p 4040:4040 -e SPARK_OPTS='--driver-java-options=-Xms1024M --driver-java-options=-Xmx4096M --driver-java-options=-Dlog4j.logLevel=info --packages graphframes:graphframes:0.6.0-spark2.3-s_2.11' -v "$PWD":/home/jovyan/work jupyter/all-spark-notebook:ports
