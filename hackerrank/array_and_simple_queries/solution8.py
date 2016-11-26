#!/usr/bin/env python
#
# Using an implicit treap implemented with arrays.
#
# Source: https://threads-iiith.quora.com/Treaps-One-Tree-to-Rule-em-all-Part-2

from collections import deque


# Implicit treap global arrays
left = right = priority = size = None


def init_treap(length):

    global left, right, priority, size

    left = [None] * length
    right = [None] * length
    priority = [None] * length
    size = [1] * length
    root = length / 2

    stack = deque()
    stack.append((0, root, length - 1))

    highest_priority = length

    while stack:

        (first, mid_node, last) = stack.popleft()

        size[mid_node] = last - first + 1
        priority[mid_node] = highest_priority
        highest_priority -= 1

        if mid_node > first:
            left_node = first + (mid_node - first) / 2
            left[mid_node] = left_node
            stack.append((first, left_node, mid_node - 1))

        if last > mid_node:
            right_node = last - (last - mid_node) / 2
            right[mid_node] = right_node
            stack.append((mid_node + 1, right_node, last))

    return root


def update_size(node):

    global left, right, size

    node_size = 1
    if left[node] is not None:
        node_size += size[left[node]]
    if right[node] is not None:
        node_size += size[right[node]]

    size[node] = node_size


def split(root, position, add=0):

    global left, right, size

    if root is None:
        return None, None

    curr_pos = add
    if left[root] is not None:
        curr_pos += size[left[root]]

    if curr_pos < position:
        if right[root] is None:
            return root, None
        left_root = root
        right[root], right_root = split(right[root], position, curr_pos + 1)
    else:
        if left[root] is None:
            return None, root
        right_root = root
        left_root, left[root] = split(left[root], position, add)

    update_size(root)

    return left_root, right_root


def merge(left_root, right_root):

    global left, right, priority

    if left_root is None:
        return right_root

    if right_root is None:
        return left_root

    if priority[left_root] > priority[right_root]:
        root = left_root
        right[left_root] = merge(right[left_root], right_root)
    else:
        root = right_root
        left[right_root] = merge(left_root, left[right_root])

    update_size(root)

    return root


def get_values(root):

    global left, right

    return ((get_values(left[root]) if left[root] is not None else []) +
            [root] +
            (get_values(right[root]) if right[root] is not None else []))

def main():

    global left, right, priority, size

    _, queries = [int(x) for x in raw_input().split()]
    array = [int(x) for x in raw_input().split()]

    array_len = len(array)

    root = init_treap(array_len)

    for _ in xrange(queries):

        oper, pos_i, pos_j = [int(x) for x in raw_input().split()]

        if oper == 1:
            if pos_i > 1:
                left_root, mid_root = split(root, pos_i - 1)
                mid_root, right_root = split(mid_root, pos_j - pos_i + 1)
                root = merge(mid_root, left_root)
                root = merge(root, right_root)
        else:
            if pos_j < array_len:
                left_root, mid_root = split(root, pos_i - 1)
                mid_root, right_root = split(mid_root, pos_j - pos_i + 1)
                root = merge(left_root, right_root)
                root = merge(root, mid_root)

    indices = get_values(root)

    print abs(array[indices[0]] - array[indices[array_len - 1]])
    print " ".join(str(array[idx]) for idx in indices)


if __name__ == '__main__':

    main()
