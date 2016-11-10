#!/usr/bin/env python

from time import time
from random import randint


NUM_TESTS = 10 ** 4
DIM = 10 ** 5
MAX_NUM = 10 ** 9

buffer = [0] * DIM


class Node:

    __slots__ = ['value', 'prev', 'next']

    def __init__(self, value, prev):
        self.value = value
        self.prev = prev
        self.next = None


def move_to_start_list(head, tail, pos_i, pos_j):

    if pos_i <= 1:
        return head, tail

    pos = 1
    node_i = head
    while pos < pos_i:
        node_i = node_i.next
        pos += 1

    node_j = node_i
    while pos < pos_j:
        node_j = node_j.next
        pos += 1

    if node_j.next:
        node_j.next.prev = node_i.prev
    else:
        tail = node_i.prev

    node_i.prev.next = node_j.next
    node_i.prev = None

    node_j.next = head
    head.prev = node_j

    return node_i, tail


def move_to_end_list(list_len, head, tail, pos_i, pos_j):

    if pos_j >= list_len:
        return head, tail

    pos = list_len
    node_j = tail
    while pos > pos_j:
        node_j = node_j.prev
        pos -= 1

    node_i = node_j
    while pos > pos_i:
        node_i = node_i.prev
        pos -= 1

    if node_i.prev:
        node_i.prev.next = node_j.next
    else:
        head = node_j.next

    node_j.next.prev = node_i.prev
    node_j.next = None

    node_i.prev = tail
    tail.next = node_i

    return head, node_j


def move_to_start_array(numbers, pos_i, pos_j):

    count = pos_j - pos_i + 1
    buffer[:count] = numbers[pos_i - 1:pos_j]
    numbers[count:pos_j] = numbers[:pos_i - 1]
    numbers[:count] = buffer[:count]


def move_to_end_array(numbers, pos_i, pos_j):

    count = pos_j - pos_i + 1
    buffer[:count] = numbers[pos_i - 1:pos_j]
    numbers[pos_i - 1:len(numbers) - count] = numbers[pos_j:]
    numbers[-count:] = buffer[:count]


# Main program

array = [0] * DIM
for i in xrange(DIM):
    array[i] = randint(1, MAX_NUM)

prev = head = Node(array[0], prev=None)
for idx in xrange(1, DIM):
    node = Node(array[idx], prev)
    prev.next = node
    prev = node
tail = prev

time_1 = time_2 = 0

for _ in xrange(NUM_TESTS):

    oper = randint(1,2)
    pos_i = randint(1, DIM)
    pos_j = randint(pos_i, DIM)

    start = time()
    if oper == 1:
        move_to_start_array(array, pos_i, pos_j)
    else:
        move_to_end_array(array, pos_i, pos_j)
    time_1 += time() - start

    start = time()
    if oper == 1:
        head, tail = move_to_start_list(head, tail, pos_i, pos_j)
    else:
        head, tail = move_to_end_list(DIM, head, tail, pos_i, pos_j)
    time_2 += time() - start

    #node = head
    #for idx in xrange(DIM):
    #    assert array[idx] == node.value
    #    node = node.next

print "Total time method 1: %.2f" % time_1
print "Total time method 2: %.2f" % time_2
