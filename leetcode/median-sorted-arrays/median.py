#!/usr/bin/env python

from solution2 import Solution


def main():

    solution = Solution()

    input_size = input()

    avg_time = 0

    for _ in xrange(input_size):
        nums1 = [int(x) for x in raw_input().split()]
        nums2 = [int(x) for x in raw_input().split()]

        print "%.1f" % solution.findMedianSortedArrays(nums1, nums2)


if __name__ == '__main__':

    main()
