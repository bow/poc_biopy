#!/usr/bin/env python

from __future__ import print_function

from biopy.seqio import parse


for rec in parse('test.fa', 'fasta'):
    print(str(rec.seq), len(rec))
