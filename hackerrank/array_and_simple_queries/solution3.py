#!/usr/bin/env python
#
# Using a doubly linked list implemented with arrays of indices.

import sys


def find_positions(prev, next, list_len, head, tail, pos_i, pos_j):

    idx_i = idx_j = None

    if pos_i <= list_len - pos_i:

        # seek position i from left to right
        pos = 0
        idx_i = head
        while pos < pos_i:
            idx_i = next[idx_i]
            pos += 1

        if pos_j - pos_i <= list_len - pos_j:

            # keep seeking for position j from left to right
            idx_j = idx_i
            while pos < pos_j:
                idx_j = next[idx_j]
                pos += 1

    if not idx_j:

        # seek position j from from right to left
        pos = list_len - 1
        idx_j = tail
        while pos > pos_j:
            idx_j = prev[idx_j]
            pos -= 1

        if not idx_i:

            # if needed, keep seeking position i from right to left
            idx_i = idx_j
            while pos > pos_i:
                idx_i = prev[idx_i]
                pos -= 1

    return idx_i, idx_j


def move_to_start(prev, next, head, tail, idx_i, idx_j):

    if idx_i == head:
        return head, tail

    if next[idx_j] is not None:
        prev[next[idx_j]] = prev[idx_i]
    else:
        tail = prev[idx_i]

    next[prev[idx_i]] = next[idx_j]
    prev[idx_i] = None

    next[idx_j] = head
    prev[head] = idx_j

    return idx_i, tail


def move_to_end(prev, next, head, tail, idx_i, idx_j):

    if idx_j == tail:
        return head, tail

    if prev[idx_i] is not None:
        next[prev[idx_i]] = next[idx_j]
    else:
        head = next[idx_j]

    prev[next[idx_j]] = prev[idx_i]
    next[idx_j] = None

    prev[idx_i] = tail
    next[tail] = idx_i

    return head, idx_j


# Main program

_, queries = [int(x) for x in raw_input().split()]

numbers = [int(x) for x in raw_input().split()]

list_len = len(numbers)

prev = [None] + range(list_len - 1)
next = range(1, list_len) + [None]
head = 0
tail = list_len - 1

for _ in xrange(queries):

    oper, pos_i, pos_j = [int(x) for x in raw_input().split()]

    # Map positions to zero-based arrays
    pos_i -= 1
    pos_j -= 1

    # Find indices of positions
    idx_i, idx_j = find_positions(prev, next, list_len, head, tail, pos_i, pos_j)

    if oper == 1:
        head, tail = move_to_start(prev, next, head, tail, idx_i, idx_j)
    else:
        head, tail = move_to_end(prev, next, head, tail, idx_i, idx_j)

print abs(numbers[tail] - numbers[head])
sys.stdout.write("%d" % numbers[head])
pos = next[head]
while pos is not None:
    sys.stdout.write(" %d" % numbers[pos])
    pos = next[pos]
sys.stdout.write('\n')
