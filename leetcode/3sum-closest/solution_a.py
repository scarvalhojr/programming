#!/usr/bin/env python

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
            for i2 in range(i1 + 1, length):
                for i3 in range(i2 + 1, length):

                    candidate = n1 + nums[i2] + nums[i3]
                    dist = abs(target - candidate)

                    #print "candidate = %d + %d + %d = %d" % (n1, nums[i2], nums[i3], candidate)
                    #print "dist = abs(%d - %d) = %d" % (target, candidate, dist)

                    if dist < closest_dist:

                        if dist == 0:
                            return candidate

                        closest_sum = candidate
                        closest_dist = dist
                        #print "=> closest_sum = %d, closes_dist = %d" % (candidate, closest_dist)

        return closest_sum
