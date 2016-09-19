#!/usr/bin/env python

# chain_len[i] is the length of a chain starting at i; e.g., the chain starting
# at 6 has length 9 (6, 3, 10, 5, 16, 8, 4, 2, 1), so chain_len[6] = 9
chain_len = {1: 1}

def next_number(num):
    """ Return the next number in the Collatz sequence. """

    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1


def calc_chain_len(num):
    """ Calculate the length of a chain starting at a given number. """

    # Check if the length has been calculated before
    length = chain_len.get(num)
    if length:
        return length

    # If not, calculate it recursively
    length = calc_chain_len(next_number(num)) + 1

    # Keep track of the chain length
    chain_len[num] = length

    return length


def find_longest_chain(num):
    """ Find the longest chain starting at a number i <= num. """

    max_number = None
    max_length = 0

    for n in range(num, 1, -1):
        length = calc_chain_len(n)
        #print "DEBUG {}: {} {}".format(n, length, build_chain(n))
        if length > max_length:
            max_length = length
            max_number = n

    return max_number, max_length


def build_chain(num):
    """ Return a list with the Collatz sequence starting a given number. Only
        needed for debugging purposes.
    """

    chain = []
    chain.append(num)
    while num != 1:
        num = next_number(num)
        chain.append(num)

    return chain


# Main program

input_size = input()

for i in range(int(input_size)):
    num = input()
    max_num, _ = find_longest_chain(int(num))
    print max_num
