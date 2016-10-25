#!/usr/bin/env python

from sys import stdout

VALID_MOVES = [13, 11, 7, 5, 3, 2]
MAX_VAL_1 = 9
MAX_VAL_2 = 9
MAX_VAL_3 = 9
MAX_VAL_4 = 9
WIN_POS = '1'
LOSE_POS = '.'


def is_winning_position(pos, position_win=None, valid_moves=VALID_MOVES):

    if not position_win:
        position_win = {tuple(): False}

    # buckets with 0 or 1 balls can be ignored as they contain no moves at all;
    # also, sort the buckets to avoid computing the same bucket more than once
    pos = tuple(sorted([x for x in pos if x > 1]))

    win = position_win.get(pos)
    if win is not None:
        return win

    for b in range(len(pos)):
        for move in VALID_MOVES:
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


def print_pattern():

    position_win = {tuple(): False}

    stdout.write('      ')
    for c3 in range(MAX_VAL_3):
        for c4 in range(MAX_VAL_4):
            stdout.write('%d' % (c3 % 10))
        stdout.write(' ')
    stdout.write('\n')

    stdout.write('      ')
    for c3 in range(MAX_VAL_3):
        for c4 in range(MAX_VAL_4):
            stdout.write('%d' % (c4 % 10))
        stdout.write(' ')
    stdout.write('\n')

    for c1 in range(MAX_VAL_1):
        for c2 in range(MAX_VAL_2):
            stdout.write('%2d %2d ' % (c1,c2))
            for c3 in range(MAX_VAL_3):
                for c4 in range(MAX_VAL_4):
                    if is_winning_position((c1,c2,c3,c4), position_win):
                        stdout.write('%s' % WIN_POS)
                    else:
                        stdout.write('%s' % LOSE_POS)
                stdout.write(' ')
            stdout.write('\n')
        stdout.write('\n')


if __name__ == '__main__':

    print_pattern()
