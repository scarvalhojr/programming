#!/usr/bin/env python
#
# Pure brute force, copying array blocks.

MAX_DIM = 10 ** 5

buffer = [0] * MAX_DIM


def move_to_start(numbers, pos_i, pos_j):

    count = pos_j - pos_i + 1
    buffer[:count] = numbers[pos_i - 1:pos_j]
    numbers[count:pos_j] = numbers[:pos_i - 1]
    numbers[:count] = buffer[:count]


def move_to_end(numbers, pos_i, pos_j):

    count = pos_j - pos_i + 1
    buffer[:count] = numbers[pos_i - 1:pos_j]
    numbers[pos_i - 1:len(numbers) - count] = numbers[pos_j:]
    numbers[-count:] = buffer[:count]


def main():

    _, queries = [int(x) for x in raw_input().split()]

    numbers = [int(x) for x in raw_input().split()]

    for _ in xrange(queries):
        oper, pos_i, pos_j = [int(x) for x in raw_input().split()]
        if oper == 1:
            move_to_start(numbers, pos_i, pos_j)
        else:
            move_to_end(numbers, pos_i, pos_j)

    print abs(numbers[0] - numbers[len(numbers) - 1])
    print " ".join(str(x) for x in numbers)


if __name__ == '__main__':

    main()
