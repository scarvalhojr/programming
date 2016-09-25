#!/usr/bin/env python
#
# Smarter brute force:
# 1) inferring if element is divisible without calculating its actual value;
# 2) only testing up to half of the elements in each row.

from math import log


# This is the number we're counting how many elements
# of the triangle cannot be divided by
DIV = 7

def is_non_divisible(row, col):

    # formula to calculate element at (row,col): row! / (col! x (row - col)!)

    # how many multiples of DIV can the element be factored into?
    multiples = 0

    # count how many multiples of every power of DIV
    # (e.g. 7^1, 7^2...) each factor of the formula has
    for power in range(1, 1 + int(log(row,DIV))):
        m = DIV ** power
        multiples += (row / m) - (col / m) - ((row - col) / m)

    return False if multiples > 0 else True


def count_non_div(rows, cols):

    if rows <= 0 or cols <= 0:
        return 0

    # element at (0,0) is 1 and cannot be divided
    count = 1

    for r in range(1, rows):

        # every row starts and ends with 1 unless
        # we're on an incomplete row
        if cols <= r:
            count += 1
        else:
            count += 2

        for c in range(1, min((r+1)/2, cols)):
            if is_non_divisible(r, c):
                if (r - c + 1) <= cols:
                    count += 2
                else:
                    count += 1

        # account for the middle element on rows
        # with odd number of columns
        if r % 2 == 0:
            c = r / 2
            if c < cols and is_non_divisible(r, c):
                count += 1

    return count


def main():

    input_size = input()

    for _ in range(input_size):
        rows, cols = [int(x) for x in raw_input().split()]
        print count_non_div(rows, cols)


if __name__ == '__main__':

    main()
