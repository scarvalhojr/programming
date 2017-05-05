#!/usr/bin/env python
#
# Even more functional-like...

import sys


def num_layers(num_rows, num_cols):

    return min(num_rows, num_cols) / 2


def len_layer(num_rows, num_cols, layer):

    return 2 * (num_rows + num_cols - 2 - 4 * layer)


def get_area_row_col(num_rows, num_cols, row, col):

    if row < num_rows / 2:
        if col < num_cols / 2 and col < row:
            return 4
        elif col >= num_cols - row:
            return 2
        else:
            return 1
    else:
        if col < num_cols / 2 and col < num_rows - row - 1:
            return 4
        elif col > num_cols - num_rows + row:
            return 2
        else:
            return 3


def get_layer_index(num_rows, num_cols, row, col):

    area = get_area_row_col(num_rows, num_cols, row, col)

    if area == 1:
        layer = row
        index = col - row
    elif area == 2:
        layer = num_cols - col - 1
        index = num_cols - 3 * layer + row - 1
    elif area == 3:
        layer = num_rows - row - 1
        index = 2 * num_cols + num_rows - 3 - 5 * layer - col
    else:
        layer = col
        index = 2 * (num_cols + num_rows) - 4 - 7 * layer - row

    return layer, index


def get_area_layer_index(num_rows, num_cols, layer, index):

    if index < num_cols - 2 * layer:
        return 1
    elif index < num_cols + num_rows - 4 * layer - 1:
        return 2
    elif index < 2 * num_cols + num_rows - 6 * layer - 2:
        return 3
    else:
        return 4


def get_row_col(num_rows, num_cols, layer, index):

    area = get_area_layer_index(num_rows, num_cols, layer, index)

    if area == 1:
        row = layer
        col = row + index
    elif area == 2:
        col = num_cols - layer - 1
        row = index - num_cols + 3 * layer + 1
    elif area == 3:
        row = num_rows - layer - 1
        col = 2 * num_cols + num_rows - 3 - 5 * layer - index
    else:
        col = layer
        row = 2 * (num_cols + num_rows) - 4 - 7 * layer - index

    return row, col


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
            layer, idx = get_layer_index(num_rows, num_cols, row, col)
            idx = (idx + rotation) % len_layer(num_rows, num_cols, layer)
            rot_row, rot_col = get_row_col(num_rows, num_cols, layer, idx)
            sys.stdout.write("%d " % matrix[rot_row][rot_col])
        sys.stdout.write("\n")

if __name__ == '__main__':

    main()
