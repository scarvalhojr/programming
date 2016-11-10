#!/usr/bin/env python

from random import randint


NUM_TESTS = 10 ** 5
DIM = 10 ** 5
MAX_NUM = 10 ** 9


print "%d %d" % (DIM, NUM_TESTS)
print " ".join([str(randint(1, MAX_NUM)) for _ in xrange(DIM)])
for _ in xrange(NUM_TESTS):
    oper = randint(1, 2)
    pos_i = randint(1, DIM)
    pos_j = randint(pos_i, DIM)
    print "%d %d %d" % (oper, pos_i, pos_j)
