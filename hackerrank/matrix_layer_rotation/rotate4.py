#!/usr/bin/env python
#
# Even more functional-like...

import sys


def len_layer(num_rows, num_cols, layer):

    return 2 * (num_rows + num_cols - 2 - 4 * layer)


def get_layer_index(num_rows, num_cols, row, col):

    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    if row < num_rows / 2:
        if col < num_cols / 2 and col < row:
            area = LEFT
        elif col >= num_cols - row:
            area = RIGHT
        else:
            area = TOP
    else:
        if col < num_cols / 2 and col < num_rows - row - 1:
            area = LEFT
        elif col > num_cols - num_rows + row:
            area = RIGHT
        else:
            area = BOTTOM

    if area == TOP:
        layer = row
        index = col - row
    elif area == RIGHT:
        layer = num_cols - col - 1
        index = num_cols - 3 * layer + row - 1
    elif area == BOTTOM:
        layer = num_rows - row - 1
        index = 2 * num_cols + num_rows - 3 - 5 * layer - col
    else:
        layer = col
        index = 2 * (num_cols + num_rows) - 4 - 7 * layer - row

    return layer, index


def get_row_col(num_rows, num_cols, layer, index):

    if index < num_cols - 2 * layer:
        # Top
        row = layer
        col = row + index
    elif index < num_cols + num_rows - 4 * layer - 1:
        # Right
        col = num_cols - layer - 1
        row = index - num_cols + 3 * layer + 1
    elif index < 2 * num_cols + num_rows - 6 * layer - 2:
        # Bottom
        row = num_rows - layer - 1
        col = 2 * num_cols + num_rows - 3 - 5 * layer - index
    else:
        # Left
        col = layer
        row = 2 * (num_cols + num_rows) - 4 - 7 * layer - index

    return row, col


def rotate(num_rows, num_cols, row, col, rotation):

    layer, idx = get_layer_index(num_rows, num_cols, row, col)
    idx = (idx + rotation) % len_layer(num_rows, num_cols, layer)
    return get_row_col(num_rows, num_cols, layer, idx)


def main():

    (num_rows, num_cols, rotation) = (int(x) for x in raw_input().split())

    assert min(num_rows, num_cols) % 2 == 0

    matrix = []

    for row in range(num_rows):
        line = [int(x) for x in raw_input().split()]
        assert len(line) == num_cols
        matrix.append(line)

    for row in range(num_rows):
        for col in range(num_cols):
            rot_row, rot_col = rotate(num_rows, num_cols, row, col, rotation)
            sys.stdout.write("%d " % matrix[rot_row][rot_col])
        sys.stdout.write("\n")

if __name__ == '__main__':

    main()
