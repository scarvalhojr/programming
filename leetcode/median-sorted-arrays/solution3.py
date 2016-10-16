# Solution 3
#
# Iterate over the sorted arrays until the middle point is reached.

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        len1 = len(nums1)
        len2 = len(nums2)
        total_len = len1 + len2

        if total_len == 0:
            return None

        median = pos1 = pos2 = 0

        phase_1 = min((total_len - 1) / 2, len1, len2)

        for _ in xrange(phase_1):
            if nums1[pos1] < nums2[pos2]:
                pos1 += 1
            else:
                pos2 += 1

        phase_2 = ((total_len - 1) / 2) - phase_1

        for _ in xrange(phase_2):
            if pos1 < len1 and pos2 < len2:
                if nums1[pos1] < nums2[pos2]:
                    pos1 += 1
                else:
                    pos2 += 1
            elif pos1 < len1:
                pos1 += 1
            else:
                pos2 += 1

        phase_3 = 2 if total_len % 2 == 0 else 1

        for _ in xrange(phase_3):
            if pos1 < len1 and pos2 < len2:
                if nums1[pos1] < nums2[pos2]:
                    median += nums1[pos1]
                    pos1 += 1
                else:
                    median += nums2[pos2]
                    pos2 += 1
            elif pos1 < len1:
                median += nums1[pos1]
                pos1 += 1
            else:
                median += nums2[pos2]
                pos2 += 1

        if total_len % 2 == 0:
            return median / 2.0
        else:
            return median
