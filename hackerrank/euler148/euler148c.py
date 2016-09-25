#!/usr/bin/env python
#
# Smarter brute-force:
# 1) inferring if element is divisible without calculating its actual value;
# 2) faster inference by computing the multiples in the numerator once per row;
# 3) only testing up to half of the elements in each row.

from math import log


# This is the number we're counting how many elements
# of the triangle cannot be divided by
DIV = 7


def multiples_in_denominator(row, col, max_power):

    multiples = 0

    for power in range(1, max_power):
        m = DIV ** power
        multiples += (col / m) + ((row - col) / m)

    return multiples


def count_non_div(rows, cols):

    if rows <= 0 or cols <= 0:
        return 0

    # element at (0,0) is 1 and cannot be divided
    count = 1

    for r in range(1, rows):

        # every row starts and ends with 1 unless
        # we're on an incomplete row (cols < rows)
        if cols <= r:
            count += 1
        else:
            count += 2

        max_power = 1 + int(log(r,DIV))
        multiples_in_numerator = 0

        # count how many multiples of every power of DIV
        # (e.g. 7^1, 7^2...) elements of row have in the numerator
        for power in range(1, max_power):
            multiples_in_numerator += (r / DIV ** power)

        for c in range(1, min((r + 1)/2, cols)):
            if multiples_in_numerator - multiples_in_denominator(r, c, max_power) <= 0:
                if (r - c + 1) <= cols:
                    count += 2
                else:
                    count += 1

        # account for the middle element on rows
        # with odd number of columns
        if r % 2 == 0:
            c = r / 2
            if c < cols:
                if multiples_in_numerator - multiples_in_denominator(r, c, max_power) <= 0:
                    count += 1

    return count


def main():

    input_size = input()

    for _ in range(input_size):
        rows, cols = [int(x) for x in raw_input().split()]
        print count_non_div(rows, cols)


if __name__ == '__main__':

    main()
