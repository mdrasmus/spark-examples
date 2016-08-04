#!/usr/bin/bash

python make-data.py

../src/spark-2.0.0-bin-hadoop2.7/bin/spark-submit --master local[4] calc-synteny.py

./make-windows.py 10 H < data/s1.txt > all.sim.windows
./make-windows.py 10 M < data/s2.txt >> all.sim.windows
./make-windows.py 10 M < data/s2.txt revcomp >> all.sim.windows
