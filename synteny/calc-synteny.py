from __future__ import print_function

#from datascience import *
#from datascience.predicates import are
import numpy as np
import matplotlib
matplotlib.use('Agg', warn=False)
import matplotlib.pyplot as plots
#plots.style.use('fivethirtyeight')
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
import random
from collections import defaultdict

import matplotlib.pyplot as plt
import seaborn as sns


from pyspark.sql import SparkSession

comp = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}

def revcomp(seq):
    return ''.join(comp[a] for a in reversed(seq))

def line_to_kv(line):
    seq = line.split(',')
    return seq[1], (int(seq[0]), seq[1], seq[2])

def find_matches(kv):
    _, grouped = kv
    matches = []
    grouped = list(grouped)
    humans = [row[0] for row in grouped if row[2] == 'H']
    mice = [row[0] for row in grouped if row[2] == 'M']
    for human in humans:
        for mouse in mice:
            matches.append((human, mouse))
    return matches

spark = SparkSession\
    .builder\
    .appName("CalcSynteny")\
    .getOrCreate()
sc = spark.sparkContext

windows = sc.textFile('all.sim.windows')

result = (
    windows
    .map(line_to_kv)
    .groupByKey()
    .map(find_matches)
    .flatMap(lambda x: x)
    .collect()
)

x, y = zip(* result)

plt.figure(figsize=(10, 10))
plot = plt.scatter(x, y)
plot.figure.savefig('figures/sim.png')

spark.stop()
