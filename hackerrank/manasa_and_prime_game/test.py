#!/usr/bin/env python

from random import randint

from manasa1 import is_winning_position as solution_1
from manasa2 import is_winning_position as solution_2


NUM_TESTS = 100
MIN_DIM = 3
MAX_DIM = 6
MAX_VALUE = 50
VALID_MOVES_1 = [13, 11, 7, 5, 3, 2]
VALID_MOVES_2 = [7, 5, 3, 2]


def test():

    position_win_1 = {tuple(): False}
    position_win_2 = {tuple(): False}

    for _ in range(NUM_TESTS):

        dim = randint(MIN_DIM, MAX_DIM)

        pos = tuple(randint(0,MAX_VALUE) for _ in range(dim))

        res_1 = solution_1(pos, position_win_1, VALID_MOVES_1)
        res_2 = solution_2(pos, position_win_2, VALID_MOVES_2)

        if res_1 != res_2:
            print "Position: %s" % (pos,)
            print "Solution 1: %s" % res_1
            print "Solution 2: %s" % res_2

    print "%d positions learned by solution 1." % len(position_win_1)
    print "%d positions learned by solution 2." % len(position_win_2)


if __name__ == '__main__':

    test()
