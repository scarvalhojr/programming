#!/usr/bin/env python

# chain_len[i] is the length of a chain starting at i; e.g., the chain starting
# at 6 has length 9 (6, 3, 10, 5, 16, 8, 4, 2, 1), so chain_len[6] = 9
chain_len = {1: 1}

# longest_chain[i] is a tuple (n, l) where n is a number that starts the
# longest chain for n <= i, and l is the length of that chain
# e.g. longest_len[5] = (3, 8), i.e. [3, 10, 5, 16, 8, 4, 2, 1]
longest_chain = [(0, 0), (1, 1)]


def calc_chain_len(num):
    """ Calculate the length of a chain starting at a given number. """

    stack = []

    length = chain_len.get(num)

    while not length:

        stack.append(num)

        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1

        length = chain_len.get(num)

    while stack:

        num = stack.pop()

        length += 1

        chain_len[num] = length

    return length


def find_longest_chain(num):
    """ Find the longest chain starting at a number i <= num. """

    for n in range(len(longest_chain), num + 1):

        length = calc_chain_len(n)

        if longest_chain[n-1][1] > length:
            longest_chain.append(longest_chain[n-1])
        else:
            longest_chain.append((n, length))

    return longest_chain[num]


# Main program

input_size = input()

for i in range(int(input_size)):
    num = input()
    max_num, _ = find_longest_chain(int(num))
    print max_num
