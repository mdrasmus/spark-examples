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

def perc_id(s1, s2):
    assert len(s1) == len(s2)
    matches = sum(
        1
        for i in range(len(s1))
        if s1[i] == s2[i]
    )
    return matches / float(len(s1))

def calc_synteny(s1, s2, k, threshold):
    mat = []
    for i in range(len(s1) - k):
        for j in range(len(s2) - k):
            window1 = s1[i:i + k]
            window2 = s2[j:j + k]
            score1 = perc_id(window1, window2)
            score2 = perc_id(window1, revcomp(window2))
            max_score = max(score1, score2)
            if max_score > threshold:
                mat.append((i, j, max_score))
    return mat


# Make simulated data.
def make_sim():
    a = make_seq(1000)
    b = make_seq(1000)
    s1 = a + b
    s2 = a + revcomp(b)

    with open('data/s1.txt', 'w') as out:
        out.write(s1)

    with open('data/s2.txt', 'w') as out:
        out.write(s2)


make_sim()
