#!/usr/bin/env python

from sys import stdout
from random import randint


NUM_TESTS = 10
MAX_NUMBER = 5 * 10 ** 7
NUM_ELEMS_1 = 10 ** 6
NUM_ELEMS_2 = 10 ** 6 + 1

numbers = range(-MAX_NUMBER, MAX_NUMBER + 1)
array_1 = [0] * NUM_ELEMS_1
array_2 = [0] * NUM_ELEMS_2

def main():

    print NUM_TESTS

    for _ in xrange(NUM_TESTS):

        last_num = len(numbers) - 1

        for i in xrange(NUM_ELEMS_1):
            pos = randint(0, last_num)
            array_1[i] = numbers[pos]
            numbers[pos] = numbers[last_num]
            numbers[last_num] = array_1[i]
            last_num -= 1

        for i in xrange(NUM_ELEMS_2):
            pos = randint(0, last_num)
            array_2[i] = numbers[pos]
            numbers[pos] = numbers[last_num]
            numbers[last_num] = array_2[i]
            last_num -= 1

        array_1.sort()
        array_2.sort()

        for n in array_1:
            stdout.write('%d ' % n)
        stdout.write('\n')

        for n in array_2:
            stdout.write('%d ' % n)
        stdout.write('\n')


if __name__ == '__main__':

    main()
