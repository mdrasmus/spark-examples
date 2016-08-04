#!/usr/bin/env python

import sys
from itertools import islice

comp = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}

def revcomp(seq):
    return ''.join(comp[a] for a in reversed(seq))


def iter_chars(infile):
    i = 0
    while True:
        text = infile.read(1).upper()
        if not text:
            break
        yield text


def slide_window(stream, size):
    window = ''.join(islice(stream, size))
    yield window
    for c in stream:
        window = window[1:] + c
        yield window


window, tag = sys.argv[1:3]
window = int(window)

if len(sys.argv) > 3 and sys.argv[3] == 'revcomp':
    do_revcomp = True
else:
    do_revcomp = False

infile = sys.stdin


i = 0
for i, text in enumerate(slide_window(iter_chars(infile), window)):
    if 'N' in text:
        continue
    if do_revcomp:
        text = revcomp(text)
    print ','.join(map(str, [i, text, tag]))
