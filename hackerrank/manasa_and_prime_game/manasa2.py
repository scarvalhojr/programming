#!/usr/bin/env python
#
# Brute force with recursion, sorting buckets by value, reducing values to
# module 9, and ignoring buckets with 0 or 1 ball.

VALID_MOVES = [7, 5, 3, 2]


def is_winning_position(pos, position_win=None, valid_moves=VALID_MOVES):

    if not position_win:
        position_win = {tuple(): False}

    # reduce number of balls on each bucket by module 9; buckets with 0 or 1
    # balls can be ignored as they contain no moves at all; also, sort the
    # buckets to avoid computing the same bucket more than once
    pos = tuple(sorted([x % 9 for x in pos if x % 9 > 1]))

    win = position_win.get(pos)
    if win is not None:
        return win

    for b in range(len(pos)):
        for move in valid_moves:
            if pos[b] - move < 0:
                continue
            if pos[b] - move <= 1:
                next_pos = pos[:b] + pos[b + 1:]
            else:
                next_pos = pos[:b] + (pos[b] - move,) + pos[b + 1:]

            if not is_winning_position(next_pos, position_win, valid_moves):
                position_win[pos] = True
                return True

    position_win[pos] = False
    return False


def main():

    position_win = {tuple(): False}

    for _ in range(input()):
        _ = int(raw_input().strip())
        position = tuple(int(x) for x in raw_input().split())
        if is_winning_position(position, position_win):
            print 'Manasa'
        else:
            print 'Sandy'


if __name__ == '__main__':

    main()
