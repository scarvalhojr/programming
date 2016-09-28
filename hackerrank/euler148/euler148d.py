#!/usr/bin/env python
#
# Recursively decompose input into triangles of dimensions that are power of 7
# and other shapes

from math import log
from logging import getLogger, StreamHandler, DEBUG


# Debug log
#LOG = getLogger(__name__)
#LOG.addHandler(StreamHandler())
#LOG.setLevel(DEBUG)

# This is the number we're counting how many elements
# of the triangle cannot be divided by
DIV = 7

# The largest power of DIV we will attempt to decompose the input into;
# MAX_POWER is the largest power p such that DIV ^ p <= 10 ^ 18, which is
# the largest input we're supposed to handle
MAX_POWER = 22

# Results must be reported in modulo 10 ^ 9 + 7
RESULT_MOD = 10 ** 9 + 7

# Number of non-divisible elements in a "square" triangle
# (with dimensions that are a power of DIV)
square_non_div = [(((DIV ** 2 + DIV) / 2) ** power) % RESULT_MOD
                  for power in range(MAX_POWER + 1)]

# Dictionary with the number of elements in a shape
# with a given number of rows and columns
num_elements = {(0,0): 0}
for cols in range(1, DIV + 1):
    num_elements[(cols, cols)] = num_elements[(cols - 1, cols - 1)] + cols
    for rows in range(cols + 1, DIV + 1):
        num_elements[(rows,cols)] = num_elements[(rows - 1,cols)] + cols


def count_non_div(rows, cols):

    #LOG.debug("count_non_div(%d, %d)" % (rows, cols))

    #assert rows >= 0 and cols >= 0 and cols <= rows

    if rows <= DIV:
        return num_elements[(rows, cols)]

    count = 0

    # find the largest "square" triangle that
    # the given triangle can be decomposed into
    power = int(log(cols, DIV))
    dim = DIV ** power

    #LOG.debug("largest 'square' triangle has dim = %d" % dim)

    if rows > dim * DIV:
        #LOG.debug("tall triangle...")
        count += count_non_div(rows - dim * DIV, min(rows - dim * DIV, cols))
        #LOG.debug("after 1st triangle, count: %d" % count)

        rows = dim * DIV
        #LOG.debug("cut triangle to %d rows" % rows)

        if rows <= DIV:
            return (count + num_elements[(rows, cols)]) % RESULT_MOD

    # number of "square" triangles that fit
    # inside the given triangle
    triangles = num_elements[(rows/dim, cols/dim)]

    # the total number of non divisible elements, starting
    # with the elements in all "square" triangles
    count += triangles * square_non_div[power]

    #LOG.debug("%d 'square' triangles found; count = %d" % (triangles, count))

    south_rows = rows - dim * (rows / dim)
    east_cols = cols - dim * (cols / dim)
    south_cols = cols - east_cols
    east_rows = rows - south_rows + east_cols - cols

    #LOG.debug("south_rows: %d, south_cols: %d, east_rows: %d, east_cols: %d" % (south_rows, south_cols, east_rows, east_cols))

    #assert south_rows < dim and east_cols < dim
    #assert south_cols % dim == 0
    #assert east_rows % dim == 0

    if south_rows > 0:
        count += (south_cols / dim) * count_non_div(south_rows, south_rows)
        #LOG.debug("after south triangles, count: %d" % count)

        if east_cols > 0:
            count += count_non_div(south_rows, min(south_rows, east_cols))
            #LOG.debug("after south-east triangle, count: %d" % count)

    if east_rows > 0 and east_cols > 0:
        count += (east_rows / dim) * count_non_div(dim, east_cols)
        #LOG.debug("after east triangles, count: %d" % count)

    return count % RESULT_MOD


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
