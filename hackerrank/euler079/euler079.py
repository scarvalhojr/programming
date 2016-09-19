#!/usr/bin/env python

from heapq import heappush, heappop, heapify


def read_input():
    """ Read the input and return a dictionary 'next_chars' where
        next_chars[x] is a set of all characters that immediately
        follow x in a passcode attempt given in the input.
    """

    next_chars = {}

    input_size = int(raw_input())

    for _ in range(input_size):

        pwd_attempt = raw_input()

        for (idx, ch) in enumerate(pwd_attempt[:-1]):
            next_chars.setdefault(ch, set([])).add(pwd_attempt[idx + 1])

        next_chars.setdefault(pwd_attempt[-1:], set([]))

    return next_chars


def derivate_passcode(next_chars):

    # the passcode we want to crack
    passcode = []

    # list of candidates to be considered
    # for the next character of the passcode
    candidates = []

    # find characters that the passcode can begin with,
    # starting with all known characters...
    candidates = next_chars.keys()

    # ...and removinvg all characters that follow others
    for ch in next_chars.keys():
        for f in next_chars[ch]:
            if f in candidates:
                candidates.remove(f)

    # keep the candidates in a heap so that the first element
    # is always the lexicographically smallest
    heapify(candidates)

    # succeed[x] is a set of all character that
    # must succeed a in the actual passcode
    succeed = {}

    # build the 'succeed' dictionary from next_chars
    for ch in next_chars.keys():

        succeed[ch] = set()
        analyze = next_chars[ch].copy()

        while analyze:
            n = analyze.pop()
            if n == ch:
                # found a cycle: no solution possible
                return None
            if n not in succeed[ch]:
                succeed[ch].add(n)
                for f in next_chars[n]:
                    analyze.add(f)

    # now build the passcode
    while candidates:

        # pick the next character of the passcode
        # from the heap (lexicographically smallest)
        new_char = heappop(candidates)
        passcode.append(new_char)

        # insert characters that immediately follow the
        # new character as candidates for next characters...
        for n in next_chars[new_char]:

            insert = True

            # ...ensuring they do not follow any of
            # the new or existing candidates
            for c in next_chars[new_char].union(candidates).difference([n]):
                if n in succeed[c]:
                    insert = False
                    break

            if insert:
                heappush(candidates, n)

    if len(passcode) == len(next_chars):

        return ''.join(passcode)

    else:

        return None


if __name__ == '__main__':

    passcode = derivate_passcode(next_chars = read_input())
    print passcode if passcode else "SMTH WRONG"
