# Solution 4
#
# Translated from:
# https://discuss.leetcode.com/topic/5728/share-one-divide-and-conquer-o-log-m-n-method-with-clear-description/2

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)

        if m + n == 0:
            return None

        k = (m + n + 1) / 2

        v = self.find_kth(nums1, 0, m - 1, nums2, 0, n - 1, k)

        if (m + n) % 2 == 0:
            k2 = k + 1
            v2 = self.find_kth(nums1, 0, m - 1, nums2, 0, n - 1, k2)
            v = (v + v2) / 2.0

        return v


    # find the kth element int the two sorted arrays
    # let us say: A[aMid] <= B[bMid], x: mid len of a, y: mid len of b, then wen can know
    #
    # (1) there will be at least (x + 1 + y) elements before bMid
    # (2) there will be at least (m - x - 1 + n - y) = m + n - (x + y +1) elements after aMid
    # therefore
    # if k <= x + y + 1, find the kth element in a and b, but unconsidering bMid and its suffix
    # if k > x + y + 1, find the k - (x + 1) th element in a and b, but unconsidering aMid and its prefix
    def find_kth(self, A, aL, aR, B, bL, bR, k):
        if aL > aR: return B[bL + k - 1]
        if bL > bR: return A[aL + k - 1]

        aMid = (aL + aR) / 2
        bMid = (bL + bR) / 2

        if A[aMid] <= B[bMid]:
            if k <= (aMid - aL) + (bMid - bL) + 1:
                return self.find_kth(A, aL, aR, B, bL, bMid - 1, k)
            else:
                return self.find_kth(A, aMid + 1, aR, B, bL, bR, k - (aMid - aL) - 1)
        else: # A[aMid] > B[bMid]
            if k <= (aMid - aL) + (bMid - bL) + 1:
                return self.find_kth(A, aL, aMid - 1, B, bL, bR, k)
            else:
                return self.find_kth(A, aL, aR, B, bMid + 1, bR, k - (bMid - bL) - 1)
