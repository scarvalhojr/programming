#!/usr/bin/env python
#
# Pure brute force

MAX_DIM = 500000

last_row = [0] * MAX_DIM
curr_row = [0] * MAX_DIM

last_row[0] = 1
curr_row[0] = 1

def count_non_div(rows, cols, div=7):

    global last_row, curr_row

    if rows <= 0 or cols <= 0:
        return 0

    count = 1

    last_row[1] = 1

    for r in range(1, rows):

        count += 1

        for c in range(1, min(r,cols)):

            curr_row[c] = last_row[c - 1] + last_row[c]

            if curr_row[c] % div != 0:
                count += 1

            last_row[c - 1] = curr_row[c - 1]

        last_row[min(r,cols) - 1] = curr_row[min(r,cols) - 1]

        if r < cols:
            last_row[r] = 1
            count += 1

    return count


def main():

    input_size = input()

    for _ in range(input_size):

        rows, cols = [int(x) for x in raw_input().split()]

        if rows > MAX_DIM or cols > MAX_DIM:
            print -1
        else:
            print count_non_div(rows, cols)


if __name__ == '__main__':

    main()
