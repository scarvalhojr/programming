#!/usr/bin/env python

MAX_INPUT_NUMBER = 5000000


def calc_chain_len(num, chain_len):
    """ Calculate the length of a chain starting at a given number. """

    stack = []

    length = chain_len[num]

    while not length:

        stack.append(num)

        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1

        length = chain_len[num] if num <= MAX_INPUT_NUMBER else 0

    while stack:

        length += 1

        num = stack.pop()
        if num <= MAX_INPUT_NUMBER:
            chain_len[num] = length

    return length


def main():

    # chain_len[i] is the length of a chain starting at i; e.g., the chain starting
    # at 6 has length 9 (6, 3, 10, 5, 16, 8, 4, 2, 1), so chain_len[6] = 9
    chain_len = [0] * (MAX_INPUT_NUMBER + 1)
    chain_len[1] = 1

    # longest_chain[i] is the number n that starts the longest chain for n <= i;
    # e.g. the longest chain up to 5 starts at 3, so longest_len[5] = 3
    longest_chain = [0] * (MAX_INPUT_NUMBER + 1)
    longest_chain[1] = 1

    # first number i for which the longest chain is not yet known
    first_unknown_number = 2

    input_size = input()

    for _ in range(input_size):

        num = input()

        # If necessary, compute the longest chain for all numbers up to num
        for n in range(first_unknown_number, num + 1):

            length = chain_len[n]
            if not length:
                length = calc_chain_len(n, chain_len)

            if chain_len[longest_chain[n - 1]] > length:
                longest_chain[n] = longest_chain[n - 1]
            else:
                longest_chain[n] = n

        if num >= first_unknown_number:
            first_unknown_number = num + 1

        print longest_chain[num]


if __name__ == '__main__':

    main()
