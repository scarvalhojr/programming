#!/usr/bin/env python
#
# Reduce number of balls on each bucket to one of [1, 2, 3, 4], sort buckets
# by value, and solve recursively.

VALID_MOVES = [4, 3, 2, 1]


def is_winning(pos, position_win, valid_moves=VALID_MOVES):

    # reduce number of balls on each bucket to one of [1, 2, 3, 4]; also, sort
    # the buckets to avoid computing the same bucket more than once
    pos = tuple(sorted([(x % 9) / 2 for x in pos if x % 9 >= 1]))

    win = position_win.get(pos)
    if win is not None:
        return win

    return _is_winning(pos, position_win, valid_moves)


def _is_winning(pos, position_win, valid_moves):

    for b in range(len(pos)):
        for move in VALID_MOVES:
            new_val = pos[b] - move

            if new_val < 0:
                continue
            elif new_val == 0:
                next_pos = pos[:b] + pos[b + 1:]
            else:
                next_pos = pos[:b] + (new_val,) + pos[b + 1:]

            next_pos = tuple(sorted(next_pos))

            next_win = position_win.get(next_pos)
            if next_win is None:
                next_win = _is_winning(next_pos, position_win, valid_moves)

            if not next_win:
                position_win[pos] = True
                return True

    position_win[pos] = False
    return False


def main():

    position_win = {tuple(): False}

    for _ in range(input()):
        _ = int(raw_input().strip())
        position = tuple(int(x) for x in raw_input().split())
        if is_winning(position, position_win):
            print 'Manasa'
        else:
            print 'Sandy'


if __name__ == '__main__':

    main()
