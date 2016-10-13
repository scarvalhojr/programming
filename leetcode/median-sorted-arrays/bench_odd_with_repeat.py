#!/usr/bin/env python

from time import time
from random import randint
from solution1 import Solution as Solution1
from solution2 import Solution as Solution2


NUM_TESTS = 5
MAX_NUMBER = 5 * 10 ** 7
NUM_ELEMS_1 = 10 ** 7
NUM_ELEMS_2 = 10 ** 7 + 1


def main():

    print "Average time benchmark - odd total length, with repeats"
    print "%d test(s) with sizes %d and %d from range [%d, %d]" % (NUM_TESTS,
        NUM_ELEMS_1, NUM_ELEMS_2, -MAX_NUMBER, MAX_NUMBER)

    solution_1 = Solution1()
    solution_2 = Solution2()

    array_1 = [0] * NUM_ELEMS_1
    array_2 = [0] * NUM_ELEMS_2

    time_1 = time_2 = 0

    for _ in xrange(NUM_TESTS):

        for i in xrange(NUM_ELEMS_1):
            array_1[i] = randint(-MAX_NUMBER, MAX_NUMBER)

        for i in xrange(NUM_ELEMS_2):
            array_2[i] = randint(-MAX_NUMBER, MAX_NUMBER)

        array_1.sort()
        array_2.sort()

        start = time()
        res_1 = solution_1.findMedianSortedArrays(array_1, array_2)
        time_1 += time() - start

        start = time()
        res_2 = solution_2.findMedianSortedArrays(array_1, array_2)
        time_2 += time() - start

        #if res_1 != res_2:
        #    print "ERROR: Inconsistency in results."
        #    print "Array 1: %s" % ' '.join([str(x) for x in array_1])
        #    print "Array 2: %s" % ' '.join([str(x) for x in array_2])
        #    print "Solution 1: %d" % res_1
        #    print "Solution 2: %d" % res_2

        assert res_1 == res_2

    print "Solution 1: %.2f seconds" % (time_1 / NUM_TESTS)
    print "Solution 2: %.2f seconds" % (time_2 / NUM_TESTS)


if __name__ == '__main__':

    main()
