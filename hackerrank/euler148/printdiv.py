#!/usr/bin/env python

from sys import stdout

DIM = 1000
DIV = 7

NORM_CHAR = ' '
BORD_CHAR = '1'
DIV_CHAR = '@'

last_row = [0] * DIM
last_row[0] = 1

stdout.write('%4d =>  %s\n' % (0, BORD_CHAR))

for r in range(1, DIM):

    stdout.write('%4d =>  %s' % (r, BORD_CHAR))
    last_val = 1

    for c in range(1, r):

        val = last_row[c - 1] + last_row[c]
        if val % DIV == 0:
            stdout.write(' %s' % DIV_CHAR)
        else:
            stdout.write(' %s' % NORM_CHAR)

        last_row[c - 1] = last_val
        last_val = val

    last_row[r - 1] = last_val
    last_row[r] = 1
    stdout.write(' %s\n' % BORD_CHAR)
