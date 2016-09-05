#!/usr/bin/env python

MAX_INPUT_NUMBER = 5000000

# chain_len[i] is the length of a chain starting at i; e.g., the chain starting
# at 6 has length 9 (6, 3, 10, 5, 16, 8, 4, 2, 1), so chain_len[6] = 9
chain_len = [None for x in range(MAX_INPUT_NUMBER + 1)]
chain_len[1] = 1

# longest_chain[i] is the number n that starts the longest chain for n <= i;
# e.g. the longest chain up to 5 starts at 3, so longest_len[5] = 3
longest_chain = [None for x in range(MAX_INPUT_NUMBER + 1)]
longest_chain[1] = 1

# first number i for which the longest chain is not yet known
first_unknown_number = 2


def calc_chain_len(num):
    """ Calculate the length of a chain starting at a given number. """

    global chain_len

    length = 0

    prev_length = chain_len[num]

    n = num

    while not prev_length:

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

        length += 1

        prev_length = chain_len[n] if n < MAX_INPUT_NUMBER else None

    chain_len[num] = length + prev_length

    return chain_len[num]


def find_longest_chain(num):
    """ Find the longest chain starting at a number i <= num. """

    global first_unknown_number, chain_len, longest_chain

    # If necessary, compute the longest chain for all numbers up to num
    for n in range(first_unknown_number, num + 1):

        length = calc_chain_len(n)

        if chain_len[longest_chain[n - 1]] > length:
            longest_chain[n] = longest_chain[n - 1]
        else:
            longest_chain[n] = n

    first_unknown_number = num + 1

    return longest_chain[num]


# Main program

input_size = input()

for i in range(input_size):
    num = input()
    print find_longest_chain(num)
