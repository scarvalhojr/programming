#!/usr/bin/env python

def max_toys(prices, money):

    prices.sort()
    spent = 0
    count = 0
    for p in prices:
        if p + spent > money:
            break
        spent += p
        count += 1

    return count

if __name__ == '__main__':

    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
