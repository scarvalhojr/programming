# Solution 3
#
# Iterate over the sorted arrays until the middle point is reached.

from heapq import merge

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        total_len = len(nums1) + len(nums2)
        if total_len <= 0:
            return None

        iterator = merge(nums1, nums2)

        if total_len == 1:
            return iterator.next()

        for _ in xrange(total_len / 2 - 1):
            iterator.next()

        mid_1 = iterator.next()
        mid_2 = iterator.next()

        if total_len % 2 == 0:
            return (mid_1 + mid_2) / 2.0
        else:
            return mid_2
