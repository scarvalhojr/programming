#!/usr/bin/env python

import sys
from random import randint

from solution5 import NumberList
from solution1 import move_to_start, move_to_end

DIM = 100
NUM_TESTS = 1000
NUM_OPS = 100


def main():

    for _ in xrange(NUM_TESTS):

        numbers = range(0, DIM)
        num_list = NumberList(range(0, DIM))

        print "\nStarting test"

        for _ in xrange(NUM_OPS):

            pos_i = randint(0, DIM - 1)
            pos_j = randint(pos_i, DIM - 1)

            print "pos_i = %d, pos_j = %d" % (pos_i, pos_j)

            move_to_start(numbers, pos_i + 1, pos_j + 1)
            num_list.move_to_front(pos_i, pos_j)

        idx = 0
        pos = num_list.head
        while pos is not None:
            if num_list.numbers[pos] != numbers[idx]:
                print "Correct: %s " % " ".join(str(x) for x in numbers)
                sys.stdout.write("Wrong:   %d" % num_list.get_head())
                pos = num_list.next[num_list.head]
                while pos is not None:
                    sys.stdout.write(" %d" % num_list.numbers[pos])
                    pos = num_list.next[pos]
                sys.stdout.write('\n')
                return
            pos = num_list.next[pos]
            idx += 1

    print "All good."


if __name__ == '__main__':

    main()
