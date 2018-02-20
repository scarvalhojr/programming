#!/usr/bin/env python

from os import linesep
from random import randint
from subprocess import Popen, PIPE

NUM_TESTS = 100
(MIN_NUM_TOWNS,   MAX_NUM_TOWNS)   = (2, 5)
(MIN_TOWN_POS,    MAX_TOWN_POS)    = (0, 30)
(MIN_TOWN_POP,    MAX_TOWN_POP)    = (0, 20)
(MIN_NUM_CLOUDS,  MAX_NUM_CLOUDS)  = (2, 5)
(MIN_CLOUD_POS,   MAX_CLOUD_POS)   = (0, 30)
(MIN_CLOUD_RANGE, MAX_CLOUD_RANGE) = (1, 10)

def main():
    for num in range(NUM_TESTS):
        if not test(num):
            break

def test(num_test):
    prog1 = 'cloudy1'
    prog2 = 'cloudy2'

    numTowns   = randint(MIN_NUM_TOWNS, MAX_NUM_TOWNS)
    townPos    = generateRandomLine(numTowns, MIN_TOWN_POS, MAX_TOWN_POS)
    townPop    = generateRandomLine(numTowns, MIN_TOWN_POP, MAX_TOWN_POP)

    numClouds  = randint(MIN_NUM_CLOUDS, MAX_NUM_CLOUDS)
    cloudPos   = generateRandomLine(numClouds, MIN_CLOUD_POS, MAX_CLOUD_POS)
    cloudRange = generateRandomLine(numClouds, MIN_CLOUD_RANGE, MAX_CLOUD_RANGE)

    stdindata = linesep.join([str(numTowns), townPos, townPop,
                              str(numClouds), cloudPos, cloudRange])

    result1 = runProgram(prog1, stdindata)
    result2 = runProgram(prog2, stdindata)

    if result1 == result2:
        return True

    print "Test %d failed!" % num_test
    print "Input:"
    print stdindata
    print "%s output: %s" % (prog1, result1)
    print "%s output: %s" % (prog2, result2)

    return False

def runProgram(prog_name, stdindata):
    p = Popen(prog_name, stdin=PIPE, stdout=PIPE)
    (stdoutdata, _) = p.communicate(stdindata)
    return stdoutdata

def generateRandomLine(num_values, min_value, max_value):
    return ' '.join([str(randint(min_value, max_value))
                     for _ in range(num_values)])

if __name__ == "__main__":
    main()
