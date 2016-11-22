#!/usr/bin/env python
#
# Using an implicit treap with an object-oriented implementation.
#
# Source: https://threads-iiith.quora.com/Treaps-One-Tree-to-Rule-em-all-Part-2

from random import random


class ImplicitTreap:

    __slots__ = ['value', 'priority', 'left', 'right', 'size']


    def __init__(self, value):

        self.value = value
        self.priority = random()
        self.left = None
        self.right = None
        self.size = 1

    def update_size(self):

        size = 1
        if self.left:
            size += self.left.size
        if self.right:
            size += self.right.size

        self.size = size

    def split(self, position):

        return self._split(position, add=0)

    def _split(self, position, add):

        left = right = None

        curr_pos = add
        if self.left:
            curr_pos += self.left.size

        if curr_pos < position:
            if self.right:
                self.right, right = self.right._split(position, curr_pos + 1)
            left = self
        else:
            if self.left:
                left, self.left = self.left._split(position, add)
            right = self

        self.update_size()

        return left, right

    def merge_right(self, other):

        if not other:
            return self

        if self.priority > other.priority:
            if self.right:
                self.right = self.right.merge_right(other)
            else:
                self.right = other
            root = self
        else:
            if other.left:
                other.left = self.merge_right(other.left)
            else:
                other.left = self
            root = other

        root.update_size()

        return root

    def insert_at_position(self, value, position):

        left, right = self.split(position)
        root = left.merge_right(ImplicitTreap(value))
        return root.merge_right(right)

    def elems(self):

        return (self.left.elems() if self.left else []) + [self.value] + \
            (self.right.elems() if self.right else [])


def main():

    _, queries = [int(x) for x in raw_input().split()]
    array = [int(x) for x in raw_input().split()]

    array_len = len(array)

    root = ImplicitTreap(0)
    for idx in xrange(1, array_len):
        root = root.insert_at_position(idx, idx + 1)

    for _ in xrange(queries):

        oper, pos_i, pos_j = [int(x) for x in raw_input().split()]

        if oper == 1:
            if pos_i > 1:
                left, rest = root.split(pos_i - 1)
                middle, right = rest.split(pos_j - pos_i + 1)
                root = middle.merge_right(left).merge_right(right)
        else:
            if pos_j < array_len:
                left, rest = root.split(pos_i - 1)
                middle, right = rest.split(pos_j - pos_i + 1)
                root = left.merge_right(right) if left else right
                root = root.merge_right(middle)

    indices = root.elems()
    print abs(array[indices[0]] - array[indices[array_len - 1]])
    print " ".join(str(array[idx]) for idx in indices)


if __name__ == '__main__':

    main()
