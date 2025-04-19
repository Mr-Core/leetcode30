"""
2563. Count the Number of Fair Pairs (Medium)

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:
    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper


Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).


Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).


Constraints:
    1 <= nums.length <= 105
    nums.length == n
    -109 <= nums[i] <= 109
    -109 <= lower <= upper <= 109

Hint 1
Sort the array in ascending order.

Hint 2
For each number in the array, keep track of the smallest and largest numbers in the array that can form a fair pair with this number.

Hint 3
As you move to larger number, both boundaries move down.
"""

# -----------------------
# Testing 1: Brute force
# -----------------------

# nums = [0, 1, 7, 4, 4, 5]
# lower = 3
# upper = 6
#
# fair_pairs = []
#
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if 0 <= i < j < len(nums):
#             if lower <= nums[i] + nums[j] <= upper:
#                 fair_pairs.append((i, j))
#
# print(len(fair_pairs))


# ----------------------------------------------
# Solution 1: Brute force (Time Limit Exceeded)
# ----------------------------------------------

# from typing import List  # Optional
#
#
# class Solution:
#     def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
#         fair_pairs = []
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if 0 <= i < j < len(nums):
#                     if lower <= nums[i] + nums[j] <= upper:
#                         fair_pairs.append((i, j))
#         return len(fair_pairs)


# -------------------------------------
# Testing 2: Binary search with bisect
# -------------------------------------


# from bisect import bisect_left, bisect_right
#
# nums = [0, 1, 7, 4, 4, 5]
# lower = 3
# upper = 6
#
# nums.sort()
# count = 0
# n = len(nums)
#
# for i in range(n):
#     left = bisect_left(nums, lower - nums[i], i + 1)
#     right = bisect_right(nums, upper - nums[i], i + 1)
#     count += right - left
#
# print(count)


# ------------------------------------------------------
# Solution 2: Binary search with bisect (215ms runtime)
# ------------------------------------------------------

from typing import List  # Optional
from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1)
            count += right - left

        return count
