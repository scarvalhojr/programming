#!/usr/bin/env python
#
# Using a doubly linked list implemented with arrays of indices, and an array
# of pointers to selected positions on the list.

import sys


ELEMS_PER_POINTER = 700


def move_to_start(list_len, head, tail, prev, next, pointers, pos_i, pos_j):

    idx_i = find_index(list_len, head, tail, prev, next, pointers, pos_i)
    idx_j = find_index(list_len, head, tail, prev, next, pointers, pos_j)

    if next[idx_j] is not None:
        prev[next[idx_j]] = prev[idx_i]
    else:
        tail = prev[idx_i]

    next[prev[idx_i]] = next[idx_j]
    prev[idx_i] = None

    next[idx_j] = head
    prev[head] = idx_j

    block_size = pos_j - pos_i + 1

    for idx, pos in pointers.iteritems():
        if pos < pos_i:
            pointers[idx] += block_size
        elif pos <= pos_j:
            pointers[idx] -= pos_i

    return idx_i, tail


def move_to_end(list_len, head, tail, prev, next, pointers, pos_i, pos_j):

    idx_i = find_index(list_len, head, tail, prev, next, pointers, pos_i)
    idx_j = find_index(list_len, head, tail, prev, next, pointers, pos_j)

    if prev[idx_i] is not None:
        next[prev[idx_i]] = next[idx_j]
    else:
        head = next[idx_j]

    prev[next[idx_j]] = prev[idx_i]
    next[idx_j] = None

    prev[idx_i] = tail
    next[tail] = idx_i

    block_size = pos_j - pos_i + 1

    for idx, pos in pointers.iteritems():
        if pos > pos_j:
            pointers[idx] -= block_size
        elif pos >= pos_i:
            pointers[idx] += list_len - 1 - pos_j

    return head, idx_j


def find_index(list_len, head, tail, prev, next, pointers, position):

    idx = head
    pos = 0
    dist = position

    if list_len - 1 - position <= dist:
        idx = tail
        pos = list_len - 1
        dist = list_len - 1 - position

    for ptr_idx, ptr_pos in pointers.iteritems():
        ptr_dist = abs(position - ptr_pos)
        if ptr_dist < dist:
            dist = ptr_dist
            idx = ptr_idx
            pos = ptr_pos

    while pos < position:
        idx = next[idx]
        pos += 1

    while pos > position:
        idx = prev[idx]
        pos -= 1

    return idx


def main():

    _, queries = [int(x) for x in raw_input().split()]
    numbers = [int(x) for x in raw_input().split()]

    list_len = len(numbers)
    head = 0
    tail = list_len - 1
    prev = [None] + range(tail)
    next = range(1, list_len) + [None]
    pointers = {x:x for x in range(0, list_len, ELEMS_PER_POINTER)}

    for _ in xrange(queries):

        oper, pos_i, pos_j = [int(x) for x in raw_input().split()]

        # Map positions to zero-based arrays
        pos_i -= 1
        pos_j -= 1

        if oper == 1:
            if pos_i > 0:
                head, tail = move_to_start(list_len, head, tail, prev, next,
                    pointers, pos_i, pos_j)
        else:
            if pos_j < list_len - 1:
                head, tail = move_to_end(list_len, head, tail, prev, next,
                    pointers, pos_i, pos_j)

    print abs(numbers[tail] - numbers[head])
    sys.stdout.write("%d" % numbers[head])
    pos = next[head]
    while pos is not None:
        sys.stdout.write(" %d" % numbers[pos])
        pos = next[pos]
    sys.stdout.write('\n')


if __name__ == '__main__':

    main()
