#!/usr/bin/env python
#
# Reduce number of balls on each bucket to one of [1, 2, 3, 4], represent
# each position by the number of buckets containing each of those values, and
# solve recursively.

VALID_MOVES = [1, 2, 3, 4]


def is_winning(position, position_win, valid_moves=VALID_MOVES):

    # each position is represented by the number of buckets containing
    # 1, 2, 3, or 4 balls (after reduction)
    pos = [0, 0, 0, 0]

    # reduce number of balls on each bucket to one of [0, 1, 2, 3, 4], and
    # count how many buckets have each of the possible non-zero values
    for x in position:
        reduced = (x % 9) / 2
        if reduced > 0:
            pos[reduced - 1] += 1

    return _is_winning(tuple(pos), position_win, valid_moves)


def _is_winning(pos, position_win, valid_moves):

    if pos[1] == 0 and pos[2] == 0 and pos[3] == 0:
        # if there are only buckets with 1 ball left, this is a winning
        # position if and only if the number of such buckets is odd
        return True if pos[0] % 2 != 0 else False

    win = position_win.get(pos)
    if win is not None:
        return win

    for bucket in range(3, -1, -1):

        if pos[bucket] == 0:
            continue

        for move in range(VALID_MOVES[bucket], 0, -1):

            next_pos = list(pos)
            next_pos[bucket] -= 1

            remain = VALID_MOVES[bucket] - move
            if remain > 0:
                next_pos[remain - 1] += 1

            if not _is_winning(tuple(next_pos), position_win, valid_moves):
                position_win[pos] = True
                return True

    position_win[pos] = False
    return False


def main():

    position_win = {}

    for _ in range(input()):
        _ = int(raw_input().strip())
        position = [int(x) for x in raw_input().split()]
        if is_winning(position, position_win):
            print 'Manasa'
        else:
            print 'Sandy'


if __name__ == '__main__':

    main()
