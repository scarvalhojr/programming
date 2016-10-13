# Solution 1
#
# Pure brute-force: merge and sort the two arrays.

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        allnums = nums1 + nums2
        allnums.sort()

        length = len(allnums)
        if length <= 0:
            return None

        middle = length / 2
        if length % 2 == 0:
            return (allnums[middle - 1] + allnums[middle]) / 2.0
        else:
            return allnums[middle]
