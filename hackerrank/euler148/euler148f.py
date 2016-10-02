#!/usr/bin/env python
#
# Non-recursively decompose input into triangles of dimensions
# that are power of 7 and other shapes, remembering partial results

from math import log
from collections import deque


# This is the number we're counting how many elements
# of the triangle cannot be divided by
DIV = 7

# MAX_POWER is the largest power p such that DIV ^ p <= 10 ^ 18, which is
# the largest input we're supposed to handle, so DIV ^ MAX_POWER is the largest
# dimension of a square triangle we will attempt to decompose the input into
MAX_POWER = 21

# Results must be reported in modulo 10 ^ 9 + 7
RESULT_MOD = 10 ** 9 + 7

# Number of non-divisible elements in a shape of given number of rows, columns
non_div = {(0,0): 0}

# Pre-compute the number of elements in shapes up to DIV x DIV,
# all of which are non-divisible by DIV
for cols in range(1, DIV + 1):
    non_div[cols, cols] = non_div[cols - 1, cols - 1] + cols
    for rows in range(cols + 1, DIV + 1):
        non_div[rows,cols] = non_div[rows - 1,cols] + cols

# Pre-compute the number of non-divisible elements in triangles whose number of
# rows and columns is a power of DIV
for power in range(2, MAX_POWER + 1):
    non_div[DIV ** power, DIV ** power] = ((DIV ** 2 + DIV) / 2) ** power

# Stack with shapes that need to be processed
shapes = deque()

# Stack to accumulate partial results
accumulator = deque()


def accumulate(sub_shape_count):

    (mult, rows, cols, sub_shapes, count) = accumulator.pop()
    count = (count + sub_shape_count) % RESULT_MOD
    sub_shapes -= 1

    while sub_shapes == 0:

        if rows == cols:
            # Remember triangular results
            non_div[rows,cols] = count

        if not accumulator:
            return count

        sub_shape_count = mult * count

        (mult, rows, cols, sub_shapes, count) = accumulator.pop()
        count = (count + sub_shape_count) % RESULT_MOD
        sub_shapes -= 1

    accumulator.append((mult, rows, cols, sub_shapes, count))

    return None


def count_non_div(rows, cols):

    # assert cols <= rows

    if rows <= 0 or cols <= 0:
        return 0

    if (rows,cols) in non_div:
        return non_div[rows, cols]

    shapes.append((1, rows, cols))
    accumulator.append((1, rows, cols, 1, 0))

    while True:

        mult, rows, cols = shapes.pop()

        if (rows,cols) in non_div:
            result = accumulate(mult * non_div[rows,cols])
            if result:
                return result
            else:
                continue

        sub_shapes = 0
        count = 0

        # Find the dimension of the largest "square" triangle that
        # the given shape could be decomposed into
        dim = DIV ** int(log(cols, DIV))

        if rows <= dim * DIV:

            # Decompose the shape into up to four parts: central (with "square"
            # triangles), south, east, and south-east
            east_cols = cols - dim * (cols / dim)
            south_cols = cols - east_cols
            south_rows = rows - dim * (rows / dim)
            east_rows = rows - south_rows + east_cols - cols

            # Central part: use the non_div dictionary to calculate the
            # number of "square" triangles that fit inside the central part
            count = non_div[rows/dim, cols/dim] * non_div[dim,dim]
            count = count % RESULT_MOD

        else:

            # This is a "tall" shape: there are
            # no central or south parts
            east_cols = cols
            south_cols = 0

            dim = DIV ** int(log(rows, DIV))
            if rows == dim:
                dim = dim / DIV

            east_rows = dim * (rows / dim)
            south_rows = rows - east_rows

        if south_rows > 0:

            if south_cols > 0:
                # South part
                sub_shapes += 1
                shapes.append((south_cols / dim, south_rows, south_rows))

            if east_cols > 0:
                # South-east part
                sub_shapes += 1
                shapes.append((1, south_rows, min(south_rows, east_cols)))

        if east_rows > 0 and east_cols > 0:
            # East part
            sub_shapes += 1
            shapes.append((east_rows / dim, dim, east_cols))

        if sub_shapes > 0:
            accumulator.append((mult, rows, cols, sub_shapes, count))
        else:
            result = accumulate(mult * count)
            if result:
                return result


def main():

    input_size = input()
    for _ in range(input_size):
        rows, cols = [int(x) for x in raw_input().split()]
        print count_non_div(rows, cols)


if __name__ == '__main__':

    main()
