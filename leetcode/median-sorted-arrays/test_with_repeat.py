#!/usr/bin/env python

from sys import modules
from time import time
from os.path import basename, splitext
from random import randint
from solution1 import Solution as Solution1
from solution2 import Solution as Solution2


NUM_TESTS = 10 ** 6
MAX_NUMBER = 100
MAX_NUM_ELEMS = 10


def main():

    print "Random tests - arrays of random length, with repeats"
    print "%d test(s) with sizes up to %d from range [%d, %d]" % (NUM_TESTS,
        MAX_NUM_ELEMS, -MAX_NUMBER, MAX_NUMBER)

    solver_a = Solution1()
    solver_b = Solution2()

    module_a = splitext(basename(modules[solver_a.__module__].__file__))[0]
    module_b = splitext(basename(modules[solver_b.__module__].__file__))[0]

    for _ in xrange(NUM_TESTS):

        len1 = randint(0, MAX_NUM_ELEMS)
        len2 = randint(0, MAX_NUM_ELEMS)

        array_1 = [0] * len1
        array_2 = [0] * len2

        for i in xrange(len1):
            array_1[i] = randint(-MAX_NUMBER, MAX_NUMBER)

        for i in xrange(len2):
            array_2[i] = randint(-MAX_NUMBER, MAX_NUMBER)

        array_1.sort()
        array_2.sort()

        res_a = solver_a.findMedianSortedArrays(array_1, array_2)
        res_b = solver_b.findMedianSortedArrays(array_1, array_2)

        if res_a != res_b:
            print "ERROR: Inconsistency in results."
            print "Array 1: %s" % ' '.join([str(x) for x in array_1])
            print "Array 2: %s" % ' '.join([str(x) for x in array_2])
            print "%s: %.2f" % (module_a, res_a)
            print "%s: %.2f" % (module_b, res_b)
            return


if __name__ == '__main__':

    main()
