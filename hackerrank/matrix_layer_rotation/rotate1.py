#!/usr/bin/env python
#
# Pure brute-force

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


def rotate(num_rows, num_cols, matrix, rotation):

    layers = get_layers(num_rows, num_cols, matrix)

    for idx in range(len(layers)):
        rot = rotation % len(layers[idx])
        layers[idx] = layers[idx][rot:] + layers[idx][:rot]

    return reset_matrix(num_rows, num_cols, matrix, layers)


def main():

    (num_rows, num_cols, rotation) = (int(x) for x in raw_input().split())

    assert min(num_rows, num_cols) % 2 == 0

    matrix = []

    for row in range(num_rows):
        line = [int(x) for x in raw_input().split()]
        assert len(line) == num_cols
        matrix.append(line)

    rotate(num_rows, num_cols, matrix, rotation)

    for row in range(num_rows):
        print ' '.join(str(x) for x in matrix[row])


if __name__ == '__main__':

    main()
