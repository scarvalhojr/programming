#!/usr/bin/env python
#
# Decompose input into triangles of dimensions that are power of 7

from math import log
from logging import getLogger, StreamHandler, DEBUG


# This is the number we're counting how many elements
# of the triangle cannot be divided by
DIV = 7

# In a triangle with x rows and x columns where, for an integer p,
# x = DIV ^ p, there are NON_DIV_BASE ^ p elements that are not divisible by DIV
NON_DIV_BASE = (DIV ** 2 + DIV) / 2

RESULT_MOD = 10 ** 9 + 7

# Debug log
#LOG = getLogger(__name__)
#LOG.addHandler(StreamHandler())
#LOG.setLevel(DEBUG)


def count_non_div(rows, cols):

    #LOG.debug("count_non_div(%d, %d)" % (rows, cols))

    #assert cols <= rows

    if rows <= 0 or cols <= 0:
        return 0

    count = 0

    if rows <= DIV:
        for r in range(1, rows + 1):
            count += min(r,cols)
        #LOG.debug("final count: %d" % count)
        return count

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
        for r in range(1, rows + 1):
            count += min(r,cols)
        #LOG.debug("final count: %d" % count)
        return count

    # number of "square" triangles that fit
    # inside the given triangle
    triangles = 1
    for i in range(2, 1 + rows / dim):
        triangles += min(i * dim, cols) / dim

    # the total number of non divisible elements, starting
    # with the elements in all "square" triangles
    count = (count + triangles * (NON_DIV_BASE ** power)) % RESULT_MOD

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

    if east_rows > 0 and east_cols > 0:
        count += (east_rows / dim) * count_non_div(dim, east_cols)
        #LOG.debug("after east triangles, count: %d" % count)

    if south_rows > 0 and east_cols > 0:
        count += count_non_div(south_rows, min(south_rows, east_cols))
        #LOG.debug("after south-east triangle, count: %d" % count)

    return count % RESULT_MOD


def main():

    input_size = input()

    for _ in range(input_size):
        rows, cols = [int(x) for x in raw_input().split()]
        print count_non_div(rows, cols)


if __name__ == '__main__':

    main()
