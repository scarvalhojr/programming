#!/usr/bin/env python

from solution_b import Solution


def main():

    solution = Solution()

    input_size = input()

    for _ in range(input_size):
        target = int(raw_input())
        nums = [int(x) for x in raw_input().split()]
        print solution.threeSumClosest(nums, target)


if __name__ == '__main__':

    main()
