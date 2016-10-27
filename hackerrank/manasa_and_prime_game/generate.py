#!/usr/bin/env python

from collections import deque
from resource import getrusage, RUSAGE_SELF


VALID_MOVES = [8, 6, 4, 2]
MAX_DIM = 80

position_win = {tuple(): False}


def is_winning_position(pos):

    pos = tuple(sorted(pos, reverse=True))

    win = position_win.get(pos)
    if win is not None:
        return win

    return _is_winning_position(pos)


def _is_winning_position(pos):

    for b in range(len(pos)):
        for move in VALID_MOVES:
            if pos[b] - move < 0:
                continue
            if pos[b] - move == 0:
                next_pos = pos[:b] + pos[b + 1:]
            else:
                next_pos = pos[:b] + (pos[b] - move,) + pos[b + 1:]

            next_pos = tuple(sorted(next_pos, reverse=True))

            next_win = position_win.get(next_pos)
            if next_win is None:
                win = _is_winning_position(next_pos)

            if not next_win:
                position_win[pos] = True
                return True

    position_win[pos] = False
    return False


def generate_all():

    stack = deque((x,) for x in VALID_MOVES)

    num_elems = {x:0 for x in range(MAX_DIM + 1)}

    max_stack = winning = losing = 0

    while stack:

        if len(stack) > max_stack:
            max_stack = len(stack)

        pos = stack.popleft()
        num_elems[len(pos)] += 1
        if is_winning_position(pos):
            winning += 1
        else:
            losing += 1

        if len(pos) < MAX_DIM:
            for move in VALID_MOVES:
                if move <= pos[-1]:
                    stack.append(pos + (move,))

    mem_use = 56
    for dim, count in num_elems.iteritems():
        #print "%d positions of dimension %d" % (count, dim)
        mem_use += count * (56 + 8 * dim)
    print "%d positions examined (%d winning, %d losing)" % (len(position_win),
                                                             winning, losing)
    print "%d max elements in the stack" % max_stack
    print "%.2f GB memory used by position_win" % (mem_use / (1024. ** 3))
    print "%.2f GB max memory footprint" % (getrusage(RUSAGE_SELF).ru_maxrss / (1024. ** 3))


if __name__ == '__main__':

    generate_all()
