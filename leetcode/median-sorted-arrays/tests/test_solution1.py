#!/usr/bin/env python

from unittest import TestCase
from base import TestCornerCases, TestBasic, TestOddTotalLengthNoRepeat, \
    TestOddTotalLengthWithRepeat, TestEvenTotalLengthNoRepeat
from solution1 import Solution


class TestCornerCases(TestCase, TestCornerCases):

    def setUp(self):
        self.solution = Solution()


class TestBasic(TestCase, TestBasic):

    def setUp(self):
        self.solution = Solution()


class TestOddTotalLengthNoRepeat(TestCase, TestOddTotalLengthNoRepeat):

    def setUp(self):
        self.solution = Solution()


class TestOddTotalLengthWithRepeat(TestCase, TestOddTotalLengthWithRepeat):

    def setUp(self):
        self.solution = Solution()


class TestEvenTotalLengthNoRepeat(TestCase, TestEvenTotalLengthNoRepeat):

    def setUp(self):
        self.solution = Solution()


if __name__ == '__main__':

    unittest.main()
