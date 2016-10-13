# Solution 2
#
# Based on a binary search approach

from bisect import bisect_left


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        total_len = len(nums1) + len(nums2)

        if total_len == 0:
            # Both arrays are empty
            return None

        if len(nums1) == 0 or len(nums2) == 0:
            # One of the arrays is empty
            if len(nums1) == 0:
                allnums = nums2
            else:
                allnums = nums1

            middle = total_len / 2

            if total_len % 2 == 0:
                return (allnums[middle - 1] + allnums[middle]) / 2.0
            else:
                return allnums[middle]

        if nums2[-1] < nums1[0]:
            # All elements of the second array are less than elements of the
            # first array: swap them around
            tmp = nums1
            nums1 = nums2
            nums2 = tmp

        if total_len % 2 == 0:
            return self._find_median_even_total_length(nums1, nums2, total_len)
        else:
            return self._find_median_odd_total_length(nums1, nums2, total_len)


    def _find_median_even_total_length(self, nums1, nums2, total_len):

        len1 = len(nums1)
        len2 = len(nums2)

        if nums1[-1] < nums2[0]:
            # The arrays are completely disjoint
            middle = total_len / 2

            if middle < len1:
                return (nums1[middle - 1] + nums1[middle]) / 2.0
            elif middle == len1:
                return (nums1[-1] + nums2[0]) / 2.0
            else:
                middle = middle - len1
                return (nums2[middle - 1] + nums2[middle]) / 2.0

        # TODO: handle when arrays overlap
        assert False


    def _find_median_odd_total_length(self, nums1, nums2, total_len):

        if nums1[-1] < nums2[0]:
            # The arrays are completely disjoint
            middle = total_len / 2

            if middle < len(nums1):
                return nums1[middle]
            else:
                return nums2[middle - len(nums1)]

        numbers = [nums1, nums2]
        start = [0, 0]
        end = [len(nums1) - 1, len(nums2) - 1]

        array_a = 0
        array_b = 1

        pos_a = start[array_a] + (end[array_a] - start[array_a]) / 2

        while True:

            pos_b = bisect_left(numbers[array_b], numbers[array_a][pos_a],
                                lo=start[array_b], hi=end[array_b])

            left = pos_a + pos_b
            if pos_b == start[array_b] or pos_b == end[array_b]:
                if numbers[array_b][pos_b] < numbers[array_a][pos_a]:
                    left += 1
            right = total_len - left - 1
            diff = right - left

            #assert diff == 0 or diff % 2 == 0

            while diff > 0 and pos_b <= end[array_b]:
                # account for repetitions in array_b
                if numbers[array_a][pos_a] != numbers[array_b][pos_b]:
                    break
                pos_b += 1
                diff -= 2

            if diff == 0:
                return numbers[array_a][pos_a]

            if abs(diff) == 2:
                shift = diff / 2
            else:
                shift = diff / 4

            if shift < 0:
                shift = max(shift, start[array_a] - pos_a)
            elif shift > 0:
                shift = min(shift, end[array_a] - pos_a)

            if shift == 0:
                if diff > 0:
                    start[array_b] = pos_b
                else:
                    end[array_b] = pos_b
                array_a = 1
                array_b = 0
                pos_a = start[array_a] + (end[array_a] - start[array_a]) / 2
                continue

            if shift < 0:
                end[array_a] = max(0, pos_a - 1)
                end[array_b] = min(end[array_b], pos_b)
            else:
                start[array_a] = pos_a + 1
                start[array_b] = pos_b

            pos_a = pos_a + shift

        assert False
