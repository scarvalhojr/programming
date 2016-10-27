#!/usr/bin/env python

from sys import stdout

VALID_MOVES = [1,2,3,4]
MAX_VAL_1 = 10
MAX_VAL_2 = 10
MAX_VAL_3 = 10
MAX_VAL_4 = 10
WIN_POS = '1'
LOSE_POS = '.'


def is_winning(pos, position_win, valid_moves=VALID_MOVES):

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

            if not is_winning(tuple(next_pos), position_win, valid_moves):
                position_win[pos] = True
                return True

    position_win[pos] = False
    return False


def print_pattern():

    position_win = {}

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
                    if is_winning((c1,c2,c3,c4), position_win):
                        stdout.write('%s' % WIN_POS)
                    else:
                        stdout.write('%s' % LOSE_POS)
                stdout.write(' ')
            stdout.write('\n')
        stdout.write('\n')


if __name__ == '__main__':

    print_pattern()
