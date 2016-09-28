#!/usr/bin/env python

from random import randint

NUM_CASES = 100
MAX_ROWS = 1000000000000000000

print NUM_CASES

for _ in range(NUM_CASES):

    rows = randint(0, MAX_ROWS)
    cols = randint(0, rows)

    print "%d %d" % (rows, cols)
