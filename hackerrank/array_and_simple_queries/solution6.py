#!/usr/bin/env python
#
# INCOMPLETE!
#
# Using a doubly linked list implemented with arrays of indices, and a tree
# of pointers to selected positions on the list.

from sys import stdout
from math import log


class ListIndex:


    ELEMS_PER_POINTER = 700


    def __init__(self, list_len):

        self.head = 0
        self.tail = list_len - 1
        self.list_len = list_len

        self.max_pointers = (list_len / self.ELEMS_PER_POINTER) - 1

        self.pos = [None] * self.max_pointers
        self.idx = [None] * self.max_pointers
        self.pos_tmp = [None] * self.max_pointers
        self.idx_tmp = [None] * self.max_pointers

        idx = 0
        step = list_len / 2.
        while step >= self.ELEMS_PER_POINTER:

            pos = step
            while pos < list_len:
                self.idx[idx] = self.pos[idx] = int(round(pos))
                pos += 2 * step
                idx += 1

            step = step / 2.

        self.num_pointers = idx
        self.stack = [0] * self.num_pointers


    def get_closest_position(self, position):

        pos = 0
        idx = self.head
        dist = position

        if self.list_len - 1 - position <= dist:
            idx = self.tail
            pos = self.list_len - 1
            dist = self.list_len - 1 - position

        # TODO: use binary search tree here!
        for i in range(self.num_pointers):
            ptr_dist = abs(position - self.pos[i])
            if ptr_dist < dist:
                dist = ptr_dist
                idx = self.idx[i]
                pos = self.pos[i]

        return pos, idx


    def move_to_start(self, pos_i, pos_j):

        block_size = pos_j - pos_i + 1

        self.stack[0] = 0
        stack_idx = 0

        while stack_idx >= 0:

            idx = self.stack[stack_idx]
            stack_idx -= 1

            left_idx = 2 * idx + 1
            if left_idx < self.max_pointers and self.pos[left_idx] is not None:
                # add left node to the stack
                stack_idx += 1
                self.stack[stack_idx] = 2 * idx + 1

            if self.pos[idx] > pos_j:
                continue

            right_idx = 2 * idx + 2
            if right_idx < self.max_pointers and self.pos[right_idx] is not None:
                # add right node to the stack
                stack_idx += 1
                self.stack[stack_idx] = 2 * idx + 2

            if self.pos[idx] < pos_i:
                self.pos[idx] += block_size
            else:
                self.pos[idx] -= pos_i

        #self._rebalance()


    def move_to_end(self, pos_i, pos_j):

        block_size = pos_j - pos_i + 1

        self.stack[0] = 0
        stack_idx = 0

        while stack_idx >= 0:

            idx = self.stack[stack_idx]
            stack_idx -= 1

            if self.pos[2 * idx + 2] is not None:
                # add right node to the stack
                stack_idx += 1
                self.stack[stack_idx] = 2 * idx + 2

            if self.pos[idx] < pos_i:
                continue

            if self.pos[2 * idx + 1] is not None:
                # add left node to the stack
                stack_idx += 1
                self.stack[stack_idx] = 2 * idx + 1

            if self.pos[idx] > pos_j:
                self.pos[idx] -= block_size
            else:
                self.pos[idx] += self.list_len - 1 - pos_j

        #self._rebalance()


    def _rebalance(self):

        # TODO
        pass


def move_to_start(list_index, prev, next, pos_i, pos_j):

    idx_i = find_index(list_index, prev, next, pos_i)
    idx_j = find_index(list_index, prev, next, pos_j)

    if next[idx_j] is not None:
        prev[next[idx_j]] = prev[idx_i]
    else:
        list_index.tail = prev[idx_i]

    next[prev[idx_i]] = next[idx_j]
    prev[idx_i] = None

    next[idx_j] = list_index.head
    prev[list_index.head] = idx_j

    list_index.head = idx_i
    list_index.move_to_start(pos_i, pos_j)


def move_to_end(list_index, prev, next, pos_i, pos_j):

    idx_i = find_index(list_index, prev, next, pos_i)
    idx_j = find_index(list_index, prev, next, pos_j)

    if prev[idx_i] is not None:
        next[prev[idx_i]] = next[idx_j]
    else:
        list_index.head = next[idx_j]

    prev[next[idx_j]] = prev[idx_i]
    next[idx_j] = None

    prev[idx_i] = list_index.tail
    next[list_index.tail] = idx_i

    block_size = pos_j - pos_i + 1

    for idx in xrange(list_index.num_pointers):
        if list_index.pos[idx] > pos_j:
            list_index.pos[idx] -= block_size
        elif list_index.pos[idx] >= pos_i:
            list_index.pos[idx] += list_index.list_len - 1 - pos_j

    list_index.tail = idx_j


def find_index(list_index, prev, next, position):

    pos, idx = list_index.get_closest_position(position)

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
    prev = [None] + range(list_len - 1)
    next = range(1, list_len) + [None]

    list_index = ListIndex(list_len)

    for _ in xrange(queries):

        oper, pos_i, pos_j = [int(x) for x in raw_input().split()]

        # Map positions to zero-based arrays
        pos_i -= 1
        pos_j -= 1

        if oper == 1:
            if pos_i > 0:
                move_to_start(list_index, prev, next, pos_i, pos_j)
        else:
            if pos_j < list_len - 1:
                move_to_end(list_index, prev, next, pos_i, pos_j)

    print abs(numbers[list_index.tail] - numbers[list_index.head])
    stdout.write("%d" % numbers[list_index.head])
    pos = next[list_index.head]
    while pos is not None:
        stdout.write(" %d" % numbers[pos])
        pos = next[pos]
    stdout.write('\n')


if __name__ == '__main__':

    main()
