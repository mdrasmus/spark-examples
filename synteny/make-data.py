#!/usr/bin/env python

from random import randint

dna = "ACGT"

comp = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}

def revcomp(seq):
    return ''.join(comp[a] for a in reversed(seq))

def make_seq(k):
    return ''.join(dna[randint(0, 3)] for i in range(k))

a = make_seq(1000)
b = make_seq(1000)
s1 = a + b
s2 = a + revcomp(b)


print s1
print
print s2

with open('data/s1.txt') as out:
    out.write(s1)

with open('data/s2.txt') as out:
    out.write(s2)
