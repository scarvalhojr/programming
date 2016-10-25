#!/usr/bin/env python

VALID_MOVES = [7, 5, 3, 2]


def get_winning_move(pos, winning_move=None, valid_moves=VALID_MOVES):

    if not winning_move:
        winning_move = {tuple(): False}

    # buckets with 0 or 1 balls can be ignored as they contain no moves at all;
    # also, sort the buckets to avoid computing the same bucket more than once
    pos = tuple(sorted([x % 9 for x in pos if x % 9 > 1]))

    move = winning_move.get(pos)
    if move is not None:
        return move

    for b in range(len(pos)):
        for move in VALID_MOVES:
            if pos[b] - move < 0:
                continue
            if pos[b] - move <= 1:
                next_pos = pos[:b] + pos[b + 1:]
            else:
                next_pos = pos[:b] + (pos[b] - move,) + pos[b + 1:]

            if get_winning_move(next_pos, winning_move, valid_moves) is False:
                winning_move[pos] = next_pos
                return next_pos

    winning_move[pos] = False
    return False


def count_moves():

    winning_move = {tuple(): False}

    for c1 in range(2,9):
        pos = (c1,)
        get_winning_move(pos, winning_move)
        for c2 in range(2,9):
            pos = (c1,c2)
            get_winning_move(pos, winning_move)
            for c3 in range(2,9):
                pos = (c1,c2,c3)
                get_winning_move(pos, winning_move)
                for c4 in range(2,9):
                    pos = (c1,c2,c3,c4)
                    get_winning_move(pos, winning_move)
                    for c5 in range(2,9):
                        pos = (c1,c2,c3,c4,c5)
                        get_winning_move(pos, winning_move)
                        for c6 in range(2,9):
                            pos = (c1,c2,c3,c4,c5,c6)
                            get_winning_move(pos, winning_move)
                            for c7 in range(2,9):
                                pos = (c1,c2,c3,c4,c5,c6,c7)
                                get_winning_move(pos, winning_move)
                                for c8 in range(2,9):
                                    pos = (c1,c2,c3,c4,c5,c6,c7,c8)
                                    get_winning_move(pos, winning_move)
                                    for c9 in range(2,9):
                                        pos = (c1,c2,c3,c4,c5,c6,c7,c8,c9)
                                        get_winning_move(pos, winning_move)
                                        for c10 in range(2,9):
                                            pos = (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10)
                                            get_winning_move(pos, winning_move)

    max_dim = 10
    winning = [0] * (max_dim + 1)
    losing = [0] * (max_dim + 1)

    for pos in winning_move:
        next_pos = winning_move[pos]
        if next_pos == False:
            losing[len(pos)] += 1
        else:
            winning[len(pos)] += 1
        #print "%s => %s" % (pos, next_pos)

    for d in range(max_dim + 1):
        print "dim %d: %d winning, %d losing" % (d, winning[d], losing[d])


if __name__ == '__main__':

    count_moves()
