#!/bin/sh

# Download Java for Mac.
# Look for Java SE Development Kit 8u102
# http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

# https://www.java.com/en/download/mac_download.jsp

# Ensure java is up to date.
java -version
# java version "1.8.0_102"
# Java(TM) SE Runtime Environment (build 1.8.0_102-b14)
# Java HotSpot(TM) 64-Bit Server VM (build 25.102-b14, mixed mode)

# Download spark.
mkdir -p src
wget -O src/spark-2.0.0-bin-hadoop2.7.tgz \
     http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz

# Extract.
cd src/
tar zxvf spark-2.0.0-bin-hadoop2.7.tgz

# Tutorial: http://spark.apache.org/docs/latest/quick-start.html
# Test the spark shell.
bin/pyspark

:<<EOF
textFile = sc.textFile("README.md")
textFile.count()
EOF
