#!/usr/bin/env python

from bisect import insort


if __name__ == '__main__':

    n = int(raw_input())

    numbers = [0] * n
    count = 0

    while count < n:

        a = int(raw_input())
        insort(numbers, a, lo=0, hi=count)
        count += 1

        if count % 2 == 0:
            median = (numbers[count / 2] + numbers[count / 2 - 1]) / 2.0
        else:
            median = numbers[count / 2]

        print "%.1f" % median
