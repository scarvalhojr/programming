#!/usr/bin/env python

from sys import modules
from time import time
from os.path import basename, splitext
from random import randint
#from solution1 import Solution as Solution1
from solution2 import Solution as Solution2
from solution3 import Solution as Solution3


NUM_TESTS = 3
MAX_NUMBER = 5 * 10 ** 7
NUM_ELEMS_1 = 10 ** 7
NUM_ELEMS_2 = 10 ** 7 + 1


def main():

    print "Average time benchmark - odd total length, with repeats"
    print "%d test(s) with sizes %d and %d from range [%d, %d]" % (NUM_TESTS,
        NUM_ELEMS_1, NUM_ELEMS_2, -MAX_NUMBER, MAX_NUMBER)

    solver_a = Solution2()
    solver_b = Solution3()

    module_a = splitext(basename(modules[solver_a.__module__].__file__))[0]
    module_b = splitext(basename(modules[solver_b.__module__].__file__))[0]

    array_1 = [0] * NUM_ELEMS_1
    array_2 = [0] * NUM_ELEMS_2

    time_a = time_b = 0

    for _ in xrange(NUM_TESTS):

        for i in xrange(NUM_ELEMS_1):
            array_1[i] = randint(-MAX_NUMBER, MAX_NUMBER)

        for i in xrange(NUM_ELEMS_2):
            array_2[i] = randint(-MAX_NUMBER, MAX_NUMBER)

        array_1.sort()
        array_2.sort()

        start = time()
        res_a = solver_a.findMedianSortedArrays(array_1, array_2)
        time_a += time() - start

        start = time()
        res_b = solver_b.findMedianSortedArrays(array_1, array_2)
        time_b += time() - start

        assert res_a == res_b

    print "%s: %.2f seconds" % (module_a, time_a / NUM_TESTS)
    print "%s: %.2f seconds" % (module_b, time_b / NUM_TESTS)


if __name__ == '__main__':

    main()
