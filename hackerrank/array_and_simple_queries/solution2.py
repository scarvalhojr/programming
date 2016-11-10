#!/usr/bin/env python
#
# Using a doubly linked list implemented with pointers.

import sys


class Node:

    __slots__ = ['value', 'prev', 'next']

    def __init__(self, value, prev):
        self.value = value
        self.prev = prev
        self.next = None


def find_positions(list_len, head, tail, pos_i, pos_j):

    node_i = node_j = None

    if pos_i <= list_len - pos_i:

        # seek position i from left to right
        pos = 1
        node_i = head
        while pos < pos_i:
            node_i = node_i.next
            pos += 1

        if pos_j - pos_i <= list_len - pos_j:

            # keep seeking for position j from left to right
            node_j = node_i
            while pos < pos_j:
                node_j = node_j.next
                pos += 1

    if not node_j:

        # seek position j from from right to left
        pos = list_len
        node_j = tail
        while pos > pos_j:
            node_j = node_j.prev
            pos -= 1

        if not node_i:

            # if needed, keep seeking position i from right to left
            node_i = node_j
            while pos > pos_i:
                node_i = node_i.prev
                pos -= 1

    return node_i, node_j


def move_to_start(head, tail, node_i, node_j):

    if node_i == head:
        return head, tail

    if node_j.next:
        node_j.next.prev = node_i.prev
    else:
        tail = node_i.prev

    node_i.prev.next = node_j.next
    node_i.prev = None

    node_j.next = head
    head.prev = node_j

    return node_i, tail


def move_to_end(head, tail, node_i, node_j):

    if node_j == tail:
        return head, tail

    if node_i.prev:
        node_i.prev.next = node_j.next
    else:
        head = node_j.next

    node_j.next.prev = node_i.prev
    node_j.next = None

    node_i.prev = tail
    tail.next = node_i

    return head, node_j


def main():

    _, queries = [int(x) for x in raw_input().split()]

    numbers = [int(x) for x in raw_input().split()]

    list_len = len(numbers)

    head = Node(numbers[0], prev=None)

    prev = head
    for idx in xrange(1, list_len):
        node = Node(numbers[idx], prev)
        prev.next = node
        prev = node
    tail = prev

    for _ in xrange(queries):
        oper, pos_i, pos_j = [int(x) for x in raw_input().split()]

        node_i, node_j = find_positions(list_len, head, tail, pos_i, pos_j)

        if oper == 1:
            head, tail = move_to_start(head, tail, node_i, node_j)
        else:
            head, tail = move_to_end(head, tail, node_i, node_j)

    print abs(tail.value - head.value)
    sys.stdout.write("%d" % head.value)
    node = head.next
    while node:
        sys.stdout.write(" %d" % node.value)
        node = node.next
    sys.stdout.write('\n')


if __name__ == '__main__':

    main()
