#!/usr/bin/env python

from bisect import bisect_left
from sys import maxint


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest_sum = None
        closest_dist = maxint
        length = len(nums)

        nums.sort()

        for i1, n1 in enumerate(nums):
            for i2 in range(i1 + 1, length - 1):

                needed = target - n1 - nums[i2]
                i3 = bisect_left(nums, needed, lo=i2+1)

                if i3 < length:

                    if nums[i3] == needed:
                        return target

                    dist = abs(needed - nums[i3])
                    if dist < closest_dist:
                        closest_sum = n1 + nums[i2] + nums[i3]
                        closest_dist = dist

                if i3 - 1 > i2:

                    dist = abs(needed - nums[i3 - 1])
                    if dist < closest_dist:
                        closest_sum = n1 + nums[i2] + nums[i3 - 1]
                        closest_dist = dist

        return closest_sum
