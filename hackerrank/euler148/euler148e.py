#!/usr/bin/env python
#
# Non-recursively decompose input into triangles of dimensions
# that are power of 7 and other shapes

from math import log
from collections import deque

# This is the number we're counting how many elements
# of the triangle cannot be divided by
DIV = 7

# MAX_POWER is the largest power p such that DIV ^ p <= 10 ^ 18, which is
# the largest input we're supposed to handle, so DIV ^ MAX_POWER is the largest
# dimension of triangles we will attempt to decompose the shapes into
MAX_POWER = 21

# Results must be reported in modulo 10 ^ 9 + 7
RESULT_MOD = 10 ** 9 + 7

# Number of non-divisible elements in a shape of given number of rows, columns
non_div = {(0,0): 0}

# Pre-compute the number of elements in shapes up to DIV x DIV,
# all of which are non-divisible by DIV
for cols in range(1, DIV + 1):
    non_div[(cols, cols)] = non_div[(cols - 1, cols - 1)] + cols
    for rows in range(cols + 1, DIV + 1):
        non_div[(rows,cols)] = non_div[(rows - 1,cols)] + cols

# Pre-compute the number of non-divisible elements in triangles whose number of
# rows and columns is a power of DIV
for power in range(2, MAX_POWER + 1):
    non_div[(DIV ** power, DIV ** power)] = ((DIV ** 2 + DIV) / 2) ** power


def count_non_div(rows, cols):

    # assert rows >= 0 and cols >= 0 and cols <= rows

    shapes = deque()
    shapes.append((1, rows, cols))

    count = 0

    while shapes:

        mult, rows, cols = shapes.pop()

        if (rows,cols) in non_div:
            count = (count + mult * non_div[(rows, cols)]) % RESULT_MOD
            continue

        # Find the dimension of the largest "square" triangle that
        # the given shape could be decomposed into
        dim = DIV ** int(log(cols, DIV))

        if rows > dim * DIV:

            # This is a "tall" shape
            dim = DIV ** int(log(rows, DIV))
            if rows == dim:
                dim = dim / DIV

            # The central part
            shapes.append((mult * (rows / dim), dim, cols))

            # The south part
            south_rows = rows - dim * (rows / dim)
            if south_rows > 0:
                shapes.append((mult, south_rows, min(south_rows, cols)))

            continue

        # Decompose the shape into four parts: central (with "square" triangles),
        # south, east, and south-east
        south_rows = rows - dim * (rows / dim)
        east_cols = cols - dim * (cols / dim)
        south_cols = cols - east_cols
        east_rows = rows - south_rows + east_cols - cols

        # Central part: we can use the non_div dictionary to calculate the
        # number of "square" triangles that fit inside the central part
        count += mult * non_div[(rows/dim, cols/dim)] * non_div[(dim,dim)]
        count = count % RESULT_MOD

        if south_rows > 0:
            # South part
            shapes.append((mult * south_cols / dim, south_rows, south_rows))

            if east_cols > 0:
                # South-east part
                shapes.append((mult, south_rows, min(south_rows, east_cols)))

        if east_rows > 0 and east_cols > 0:
            # East part
            shapes.append((mult * east_rows / dim, dim, east_cols))

    return count


def main():

    input_size = input()
    for _ in range(input_size):
        rows, cols = [int(x) for x in raw_input().split()]
        if rows <= 0 or cols <= 0:
            print 0
        else:
            print count_non_div(rows, cols)


if __name__ == '__main__':

    main()
