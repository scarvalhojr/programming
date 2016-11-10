#!/usr/bin/env python

from time import time
from random import randint


NUM_TESTS = 10 ** 4
DIM = 10 ** 5
MAX_NUM = 10 ** 9

buffer = [0] * DIM


def move_to_start_1(numbers, pos_i, pos_j):

    count = pos_j - pos_i + 1
    buffer[:count] = numbers[pos_i - 1:pos_j]
    numbers[count:pos_j] = numbers[:pos_i - 1]
    numbers[:count] = buffer[:count]


def move_to_start_2(numbers, pos_i, pos_j):

    buffer[:pos_i - 1] = numbers[:pos_i - 1]
    numbers[:pos_j - pos_i + 1] = numbers[pos_i - 1:pos_j]
    numbers[pos_j - pos_i + 1:pos_j] = buffer[:pos_i - 1]


# Main program

array_1 = [0] * DIM
array_2 = [0] * DIM

for i in xrange(DIM):
    rnd = randint(1, MAX_NUM)
    array_1[i] = rnd
    array_2[i] = rnd

time_1 = time_2 = 0

for _ in xrange(NUM_TESTS):

    pos_i = randint(1, DIM)
    pos_j = randint(pos_i, DIM)

    start = time()
    move_to_start_2(array_2, pos_i, pos_j)
    time_2 += time() - start

    start = time()
    move_to_start_1(array_1, pos_i, pos_j)
    time_1 += time() - start

    # assert array_1 == array_2

print "Total time method 1: %.2f" % time_1
print "Total time method 2: %.2f" % time_2
