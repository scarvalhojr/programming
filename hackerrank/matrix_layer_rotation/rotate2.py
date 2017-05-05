#!/usr/bin/env python
#
# A bit more functional-like...


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

        layers.append(layer)

    return layers


def get_matrix(num_rows, num_cols, layers):

    matrix = []
    for row in range(num_rows):
        matrix.append([0] * num_cols)

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

    return matrix


def rotate(lst, rotation):

    rot = rotation % len(lst)

    return lst[rot:] + lst[:rot]


def main():

    (num_rows, num_cols, rotation) = (int(x) for x in raw_input().split())

    assert min(num_rows, num_cols) % 2 == 0

    matrix = []

    for row in range(num_rows):
        line = [int(x) for x in raw_input().split()]
        assert len(line) == num_cols
        matrix.append(line)

    rotated = get_matrix(num_rows, num_cols,
                         [rotate(layer, rotation)
                          for layer in get_layers(num_rows, num_cols, matrix)])

    for row in range(num_rows):
        print ' '.join(str(x) for x in rotated[row])


if __name__ == '__main__':

    main()
