#!/usr/bin/env python
#
# Don't ask me why!


def is_winning(position):

    # each position is represented by the number of buckets containing
    # 1, 2, 3, or 4 balls (after reduction)
    pos = [0, 0, 0, 0]

    # reduce number of balls on each bucket to one of [0, 1, 2, 3, 4], and
    # count how many buckets have each of the possible non-zero values
    for x in position:
        reduced = (x % 9) / 2
        if reduced > 0:
            pos[reduced - 1] += 1

    # reduce the number of buckets on each element of the positon to module 2
    for count in range(len(pos)):
        pos[count] = pos[count] % 2

    pos = tuple(pos)
    if pos == (0,0,0,0) or pos == (1,1,1,0):
        # these are the only losing positions
        return False
    else:
        return True


def main():

    for _ in range(input()):
        _ = int(raw_input().strip())
        position = [int(x) for x in raw_input().split()]
        if is_winning(position):
            print 'Manasa'
        else:
            print 'Sandy'


if __name__ == '__main__':

    main()
