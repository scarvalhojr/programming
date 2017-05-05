#!/usr/bin/env python
#
# Stress testing rotate3

import sys
from random import randint
from copy import deepcopy
from math import log


NUM_TESTS = 1000000
MIN_DIM = 2
MAX_DIM = 20
MAX_ROTATION = 999
MIN_ELEM = 1
MAX_ELEM = 999
ELEM_FORMAT = "%%%dd" % (1 + int(log(MAX_ELEM)/log(10)))


def main():

    test = 1
    while test <= NUM_TESTS:

        num_rows = randint(MIN_DIM, MAX_DIM)
        num_cols = randint(MIN_DIM, MAX_DIM)
        if min(num_rows, num_cols) % 2 != 0:
            continue

        rotation = randint(1, MAX_ROTATION)

        matrix = []

        for row in range(num_rows):
            line = [0] * num_cols
            for col in range(num_cols):
                line[col] = randint(MIN_ELEM, MAX_ELEM)
            matrix.append(line)

        matrix_copy = deepcopy(matrix)

        # run version 1
        rotate(num_rows, num_cols, matrix, rotation)

        correct = True

        for row in range(num_rows):
            for col in range(num_cols):
                # 2, 1
                layer, idx = get_layer_index(num_rows, num_cols, row, col)
                #
                idx = (idx + rotation) % len_layer(num_rows, num_cols, layer)
                rot_row, rot_col = get_row_col(num_rows, num_cols, layer, idx)

                # compare results produced by version 1 and version 3
                if matrix_copy[rot_row][rot_col] != matrix[row][col]:
                    print "ERROR: Version 1 produced a different result to " \
                          "version 3 at postion (%d, %s): %d != %d" % (
                          row, col, matrix[row][col],
                          matrix_copy[rot_row][rot_col])

                    correct = False
                    break

            if not correct:
                break

        test += 1

        if correct:
            continue

        print "Test %d: %d x %d, %d rotation(s)" % (test, num_rows, num_cols,
            rotation)

        print "\nInput:"
        for row in range(num_rows):
            print " ".join(ELEM_FORMAT % elem for elem in matrix_copy[row])

        print "\nVersion 1 output:"
        for row in range(num_rows):
            print " ".join(ELEM_FORMAT % elem for elem in matrix[row])

        print "\nVersion 3 output:"
        for row in range(num_rows):
            for col in range(num_cols):
                layer, idx = get_layer_index(num_rows, num_cols, row, col)
                idx = (idx + rotation) % len_layer(num_rows, num_cols, layer)
                rot_row, rot_col = get_row_col(num_rows, num_cols, layer, idx)
                sys.stdout.write(ELEM_FORMAT % matrix_copy[rot_row][rot_col])
                sys.stdout.write(" ")
            sys.stdout.write("\n")

        sys.exit(1)

# version 1
def get_layers(num_rows, num_cols, matrix):

    layers = []

    for layer_num in range(min(num_rows, num_cols) / 2):

        layer = [0] * (2 * (num_rows + num_cols - 2 - 4 * layer_num))

        idx = 0

        row = layer_num
        for col in range(row, num_cols - layer_num):
            layer[idx] = matrix[row][col]
            idx += 1

        col = num_cols - layer_num - 1
        for row in range(layer_num + 1, num_rows - layer_num - 1):
            layer[idx] = matrix[row][col]
            idx += 1

        row = num_rows - layer_num - 1
        for col in range(num_cols - layer_num - 1, layer_num, -1):
            layer[idx] = matrix[row][col]
            idx += 1

        col = layer_num
        for row in range(num_rows - layer_num - 1, layer_num, -1):
            layer[idx] = matrix[row][col]
            idx += 1

        #print "layer %d: %s" % (layer_num, layer)

        layers.append(layer)

    return layers

# version 1
def reset_matrix(num_rows, num_cols, matrix, layers):

    for layer_num in range(len(layers)):

        idx = 0

        row = layer_num
        for col in range(row, num_cols - layer_num):
            matrix[row][col] = layers[layer_num][idx]
            idx += 1

        col = num_cols - layer_num - 1
        for row in range(layer_num + 1, num_rows - layer_num - 1):
            matrix[row][col] = layers[layer_num][idx]
            idx += 1

        row = num_rows - layer_num - 1
        for col in range(num_cols - layer_num - 1, layer_num, -1):
            matrix[row][col] = layers[layer_num][idx]
            idx += 1

        col = layer_num
        for row in range(num_rows - layer_num - 1, layer_num, -1):
            matrix[row][col] = layers[layer_num][idx]
            idx += 1

# version 1
def rotate(num_rows, num_cols, matrix, rotation):

    layers = get_layers(num_rows, num_cols, matrix)

    for idx in range(len(layers)):
        rot = rotation % len(layers[idx])
        layers[idx] = layers[idx][rot:] + layers[idx][:rot]

    return reset_matrix(num_rows, num_cols, matrix, layers)

# version 3
def num_layers(num_rows, num_cols):

    return min(num_rows, num_cols) / 2

# version 3
def len_layer(num_rows, num_cols, layer):

    return 2 * (num_rows + num_cols - 2 - 4 * layer)

# version 3
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

# version 3
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

# version 3
def get_area_layer_index(num_rows, num_cols, layer, index):

    if index < num_cols - 2 * layer:
        return 1
    elif index < num_cols + num_rows - 4 * layer - 1:
        return 2
    elif index < 2 * num_cols + num_rows - 6 * layer - 2:
        return 3
    else:
        return 4

# version 3
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


if __name__ == '__main__':

    main()
