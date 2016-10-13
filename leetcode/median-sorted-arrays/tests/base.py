

class TestCornerCases(object):

    def test_one_empty(self):
        nums1 = [1]
        nums2 = []

        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 1)

        result = self.solution.findMedianSortedArrays(nums2, nums1)
        self.assertEquals(result, 1)

    def test_both_empty(self):
        nums1 = []
        nums2 = []
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, None)


class TestBasic(object):

    def test_sample1(self):
        nums1 = [1, 3]
        nums2 = [2]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 2.0)

    def test_sample2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 2.5)

    def test_contained(self):
        nums1 = [2, 3]
        nums2 = [1, 4, 5]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 3.0)


class TestOddTotalLengthNoRepeat(object):

    def test_basic(self):
        nums1 = [1, 2, 4]
        nums2 = [3, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 4.0)

        nums1 = [1, 2, 4]
        nums2 = [3, 6, 8, 9, 13, 18]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 6.0)

        nums1 = [1, 2, 4, 7, 11, 14, 19]
        nums2 = [3, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 7.0)

        nums1 = [1, 2, 3, 6, 8, 10]
        nums2 = [9, 15, 28, 33, 41]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 9.0)

        nums1 = [1, 2, 3, 6, 8, 10, 12, 21, 27]
        nums2 = [4, 7, 9, 11, 13, 14, 15, 18, 22, 25, 26, 28, 30, 33, 35, 38]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 14.0)

        nums1 = [1, 2, 3, 6, 8, 10, 11, 13, 15, 18, 21, 27]
        nums2 = [17, 22, 25, 26, 28, 30, 33, 35, 38]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 18.0)


class TestOddTotalLengthWithRepeat(object):

    def test_basic(self):
        nums1 = [1, 2, 4, 5, 5]
        nums2 = [3, 5, 5, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.0)

        nums1 = [1, 2, 4, 5, 5]
        nums2 = [3, 4, 5, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.0)

        nums1 = [1, 2, 4, 4, 5]
        nums2 = [3, 5, 5, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.0)

        nums1 = [1, 2, 4, 4, 5]
        nums2 = [3, 6, 6, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.0)

        nums1 = [1, 2, 5, 5, 5]
        nums2 = [5, 5, 5, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.0)

        nums1 = [1, 5, 5, 5, 5]
        nums2 = [5, 5, 5, 5, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.0)

        nums1 = [1, 2, 3, 6, 8, 10, 11, 14, 27]
        nums2 = [4, 7, 9, 11, 14, 14, 15, 18, 22, 25, 26, 28, 30, 33, 35, 38]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 14.0)

        nums1 = [1, 2, 3, 6, 6, 6, 6, 14, 27]
        nums2 = [4, 7, 9, 11, 14, 15, 15, 18, 18, 25, 25, 30, 30, 30, 35, 38]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 14.0)

        nums1 = [1, 2, 3, 8, 8, 8, 17, 17, 17, 18, 18, 27]
        nums2 = [17, 22, 22, 22, 28, 30, 33, 33, 33]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 18.0)


class TestEvenTotalLengthNoRepeat(object):

    def test_basic(self):
        nums1 = [1, 2, 4, 5]
        nums2 = [3, 6, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 4.5)

        nums1 = [1, 2, 6]
        nums2 = [4, 8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.0)

        nums1 = [1, 2, 4, 5]
        nums2 = [3, 6]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 3.5)

        nums1 = [1, 2, 4, 5]
        nums2 = [8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 4.5)

        nums1 = [1, 2, 4, 5, 6, 7]
        nums2 = [8, 9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.5)

        nums1 = [1, 2, 4, 5, 6, 7, 8]
        nums2 = [9]
        result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(result, 5.5)
