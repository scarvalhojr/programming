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

        if len(nums1) == 0 or len(nums2) == 0:
            if total_len == 0:
                return None

            if len(nums1) == 0:
                allnums = nums2
            else:
                allnums = nums1

            middle = total_len / 2

            if total_len % 2 == 0:
                return (allnums[middle - 1] + allnums[middle]) / 2.0
            else:
                return allnums[middle]

        if total_len % 2 == 0:
            return self._find_median_pair(nums1, nums2, total_len)
        else:
            return self._find_median_single(nums1, nums2, total_len)

    def _find_median_pair(self, nums1, nums2, total_len):

        numbers = [nums1, nums2]
        start = [0, 0]
        end = [len(nums1) - 1, len(nums2) - 1]

        array_a = 0
        array_b = 1

        pos_a = (start[array_a] + end[array_a]) / 2

        while True:

            pos_b = bisect_left(numbers[array_b], numbers[array_a][pos_a],
                                lo=start[array_b], hi=end[array_b])

            left = pos_a + pos_b - 1

            if numbers[array_b][pos_b] <= numbers[array_a][pos_a]:
                left += 1
                med_1 = numbers[array_b][pos_b]
            elif pos_b > 0:
                med_1 = numbers[array_b][pos_b - 1]
            else:
                med_1 = None

            if pos_a > 0 and numbers[array_a][pos_a - 1] > med_1:
                med_1 = numbers[array_a][pos_a - 1]

            diff = total_len - 2 * left - 2

            # account for repetitions
            if numbers[array_b][pos_b] == numbers[array_a][pos_a]:

                pos_c = pos_b + 1
                while diff > 0 and pos_c <= end[array_b]:
                    if numbers[array_b][pos_c] == med_1:
                        pos_c += 1
                        diff -= 2
                    else:
                        break

                if diff == -2 and (pos_a > 0 or pos_b > 0):
                    med_1a = numbers[array_a][pos_a - 1] if pos_a > 0 else None
                    med_1b = numbers[array_b][pos_b - 1] if pos_b > 0 else None
                    med_1 = max(med_1a, med_1b)
                    diff = 0

            if diff == 0:
                return (med_1 + numbers[array_a][pos_a]) / 2.0

            if abs(diff) == 2:
                shift = diff / 2
            else:
                shift = diff / 4

            if shift < 0:
                shift = max(shift, start[array_a] - pos_a)
                end[array_b] = min(end[array_b], pos_b)
            else: # shift > 0
                shift = min(shift, end[array_a] - pos_a)
                start[array_b] = pos_b

            if shift == 0:
                # move to the other array
                array_a = 1
                array_b = 0
                pos_a = (start[array_a] + end[array_a]) / 2
                continue

            if shift < 0:
                end[array_a] = pos_a - 1
            else: # shift > 0
                start[array_a] = pos_a + 1

            pos_a = pos_a + shift

    def _find_median_single(self, nums1, nums2, total_len):

        numbers = [nums1, nums2]
        start = [0, 0]
        end = [len(nums1) - 1, len(nums2) - 1]

        array_a = 0
        array_b = 1

        pos_a = (start[array_a] + end[array_a]) / 2

        while True:

            pos_b = bisect_left(numbers[array_b], numbers[array_a][pos_a],
                                lo=start[array_b], hi=end[array_b])

            left = pos_a + pos_b

            if numbers[array_b][pos_b] < numbers[array_a][pos_a]:
                left += 1

            diff = total_len - 2 * left - 1

            while diff > 0 and pos_b <= end[array_b]:
                # account for repetitions
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
                end[array_b] = min(end[array_b], pos_b)
            else: # shift > 0
                shift = min(shift, end[array_a] - pos_a)
                start[array_b] = pos_b

            if shift == 0:
                # move to the other array
                array_a = 1
                array_b = 0
                pos_a = (start[array_a] + end[array_a]) / 2
                continue

            if shift < 0:
                end[array_a] = pos_a - 1
            else: # shift > 0
                start[array_a] = pos_a + 1

            pos_a = pos_a + shift
