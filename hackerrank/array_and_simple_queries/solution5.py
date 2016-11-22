#!/usr/bin/env python
#
# INCOMPLETE!
#
# Using a doubly linked list implemented with arrays of indices, and a
# singly-linked list of pointers to selected positions on the list.

import sys


class NumberList:
    """
    Doubly-linked list of numbers, implemented with arrays.
    """


    class ListIndex:
        """
        Singly-linked list of pointers to positions in the number list.
        """

        DEFAULT_ELEMS_PER_POINTER = 500

        def __init__(self, list_len, elems_per_pointer=DEFAULT_ELEMS_PER_POINTER):

            self.list_len = list_len
            self.elems_per_pointer = elems_per_pointer
            self.position = range(0, list_len, elems_per_pointer)
            self.length = len(self.position)
            self.head = 0
            self.next = range(1, self.length) + [None]


        def move_to_front(self, pos_i, pos_j):

            new_head, seek_i_pos, seek_i_idx, seek_j_pos, seek_j_idx = self._move_to_front(self.head, self.position, self.next, pos_i, pos_j)

            if new_head is not None:
                self.head = new_head

            return (seek_i_pos, seek_i_idx * self.elems_per_pointer,
                    seek_j_pos, seek_j_idx * self.elems_per_pointer)


        def _move_to_front(self, head, position, next, pos_i, pos_j):

            shift = pos_i
            block_size = pos_j - pos_i + 1

            new_head = None

            ptr = head
            seek_i_idx = 0
            seek_i_pos = position[0]

            while ptr is not None and position[ptr] < pos_i:
                seek_i_idx = ptr
                seek_i_pos = position[ptr]
                position[ptr] += block_size
                ptr = next[ptr]

            if seek_i_pos < pos_i:
                ptr_before_i = seek_i_idx
            else:
                ptr_before_i = None

            if ptr is not None:
                if ptr_before_i is not None and position[ptr] <= pos_j:
                    new_head = ptr
                if abs(position[ptr] - pos_i) < abs(seek_i_pos - pos_i):
                    seek_i_idx = ptr
                    seek_i_pos = position[ptr]

            seek_j_idx = seek_i_idx
            seek_j_pos = seek_i_pos

            while ptr is not None and position[ptr] <= pos_j:
                seek_j_idx = ptr
                seek_j_pos = position[ptr]
                position[ptr] -= shift
                ptr = next[ptr]

            if new_head is not None:
                next[seek_j_idx] = head
                #self.head = new_head
                next[ptr_before_i] = ptr

            if ptr is not None:
                if abs(position[ptr] - pos_j) < abs(seek_j_pos - pos_j):
                    seek_j_idx = ptr
                    seek_j_pos = position[ptr]

            return new_head, seek_i_pos, seek_i_idx, seek_j_pos, seek_j_idx


        def move_to_back(self, pos_i, pos_j):

            # TODO: implement
            pass


    def __init__(self, numbers):

        self.numbers = numbers
        self.length = len(numbers)
        self.head = 0
        self.tail = self.length - 1
        self.prev = [None] + range(self.tail)
        self.next = range(1, self.length) + [None]
        self.index = NumberList.ListIndex(self.length)


    def move_to_front(self, pos_i, pos_j):

        if pos_i <= 0:
            return

        idx_i, idx_j = self.find_indices(True, pos_i, pos_j)

        if self.next[idx_j] is not None:
            self.prev[self.next[idx_j]] = self.prev[idx_i]
        else:
            self.tail = self.prev[idx_i]

        self.next[self.prev[idx_i]] = self.next[idx_j]
        self.prev[idx_i] = None

        self.next[idx_j] = self.head
        self.prev[self.head] = idx_j

        self.head = idx_i


    def move_to_back(self, pos_i, pos_j):

        if pos_j >= self.length - 1:
            return

        # TODO: implement


    def find_indices(self, move_to_front, pos_i, pos_j):

        if move_to_front:
            seek_i_pos, seek_i_idx, seek_j_pos, seek_j_idx = self.index.move_to_front(pos_i, pos_j)
        else:
            seek_i_pos, seek_i_idx, seek_j_pos, seek_j_idx = self.index.move_to_back(pos_i, pos_j)

        dist_i = abs(seek_i_pos - pos_i)
        if pos_i < dist_i:
            seek_i_pos = 0
            seek_i_idx = self.head
        elif self.length - 1 - pos_i < dist_i:
            seek_i_pos = self.length - 1
            seek_i_idx = self.tail

        idx_i = self.seek_index(self.prev, self.next, pos_i, seek_i_pos, seek_i_idx)

        dist_j = abs(seek_j_pos - pos_j)
        if pos_j - pos_i < dist_j:
            seek_j_pos = pos_i
            seek_j_idx = idx_i
        if self.length - 1 - pos_j < dist_j:
            seek_j_pos = self.length - 1
            seek_j_idx = self.tail

        idx_j = self.seek_index(self.prev, self.next, pos_j, seek_j_pos, seek_j_idx)

        return idx_i, idx_j


    def seek_index(self, prev, next, pos, seek_pos, seek_idx):

        while seek_pos < pos:
            seek_idx = next[seek_idx]
            seek_pos += 1

        while seek_pos > pos:
            seek_idx = prev[seek_idx]
            seek_pos -= 1

        return seek_idx


    def get_head(self):

        return self.numbers[self.head]


    def get_tail(self):

        return self.numbers[self.tail]



def main():

    _, queries = [int(x) for x in raw_input().split()]
    num_list = NumberList([int(x) for x in raw_input().split()])

    for _ in xrange(queries):

        oper, pos_i, pos_j = [int(x) for x in raw_input().split()]

        # Map positions to zero-based arrays
        pos_i -= 1
        pos_j -= 1

        if oper == 1:
            num_list.move_to_front(pos_i, pos_j)
        else:
            num_list.move_to_back(pos_i, pos_j)

    print abs(num_list.get_tail() - num_list.get_head())
    sys.stdout.write("%d" % num_list.get_head())
    pos = num_list.next[num_list.head]
    while pos is not None:
        sys.stdout.write(" %d" % num_list.numbers[pos])
        pos = num_list.next[pos]
    sys.stdout.write('\n')


if __name__ == '__main__':

    main()
