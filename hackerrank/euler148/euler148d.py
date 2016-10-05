#!/usr/bin/env python
#
# Recursively decompose input into triangles of dimensions that are power of 7
# and other shapes, remebering partial results

from math import log


# This is the number we're counting how many elements
# of the triangle cannot be divided by
DIV = 7

# MAX_POWER is the largest power p such that DIV ^ p <= 10 ^ 18,
# which is the largest input, so DIV ^ MAX_POWER is the largest
# dimension of a square triangle to get decomposed shapes into
MAX_POWER = 21

# Results must be reported in modulo 10 ^ 9 + 7
RESULT_MOD = 10 ** 9 + 7

# Number of non-divisible elements in a shape of given number of rows, columns
non_div = {(0,0): 0}

# Pre-compute the number of elements in shapes up to DIV x DIV,
# all of which are non-divisible by DIV
for cols in xrange(1, DIV + 1):
    non_div[cols, cols] = non_div[cols - 1, cols - 1] + cols
    for rows in xrange(cols + 1, DIV + 1):
        non_div[rows,cols] = non_div[rows - 1,cols] + cols

# Pre-compute the number of non-divisible elements in triangles whose number of
# rows and columns is a power of DIV
for power in xrange(2, MAX_POWER + 1):
    dim = DIV ** power
    non_div[dim, dim] = (((DIV ** 2 + DIV) / 2) ** power) % RESULT_MOD


def count_non_div(rows, cols):

    # assert cols <= rows

    if rows <= 0 or cols <= 0:
        return 0

    if (rows,cols) in non_div:
        return non_div[rows, cols]

    # Find the dimension of the largest "square" triangle that
    # the given shape could be decomposed into
    dim = DIV ** int(log(cols, DIV))
    if cols < dim:
        # Account for rounding errors
        dim = dim / DIV

    count = 0

    if rows > dim * DIV:

        # This is a "tall" shape: decompose it into two parts
        dim = DIV ** int(log(rows, DIV))
        if rows <= dim:
            # Ensure shape is decomposed,
            # and also account for rounding errors
            dim = dim / DIV

        # The central part
        count = ((rows / dim) * count_non_div(dim, cols)) % RESULT_MOD

        # Remember this result
        non_div[(rows/dim) * dim, cols] = count

        # The south part
        south_rows = rows - dim * (rows / dim)
        if south_rows > 0:
            count += count_non_div(south_rows, min(south_rows, cols))
            count = count % RESULT_MOD

        return count

    # Decompose the shape into central (with "square" triangles),
    # south, east, and south-east parts
    south_rows = rows - dim * (rows / dim)
    east_cols = cols - dim * (cols / dim)
    south_cols = cols - east_cols
    east_rows = rows - south_rows + east_cols - cols

    # Central part: use the non_div dictionary to calculate the
    # number of "square" triangles that fit inside the central part
    count += non_div[rows/dim, cols/dim] * non_div[dim,dim]

    if south_rows > 0:
        # South part
        count += (south_cols / dim) * count_non_div(south_rows, south_rows)

        if east_cols > 0:
            # South-east part
            count += count_non_div(south_rows, min(south_rows, east_cols))

    if east_rows > 0 and east_cols > 0:
        # East part
        count += (east_rows / dim) * count_non_div(dim, east_cols)

    count = count % RESULT_MOD

    if rows == cols:
        # Only memorize triangular shapes
        non_div[rows,cols] = count

    return count


def main():

    input_size = input()
    for _ in xrange(input_size):
        rows, cols = [int(x) for x in raw_input().split()]
        print count_non_div(rows, cols)


if __name__ == '__main__':

    main()
