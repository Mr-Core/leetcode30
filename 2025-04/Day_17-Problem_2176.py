"""
2176. Count Equal and Divisible Pairs in an Array (Easy)

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n,
such that nums[i] == nums[j] and (i * j) is divisible by k.


Example 1:

Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.


Example 2:

Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.


Constraints:
    1 <= nums.length <= 100
    1 <= nums[i], k <= 100


Hint 1
For every possible pair of indices (i, j) where i < j, check if it satisfies the given conditions.
"""

# ----------------
# Testing 1 (omo)
# ----------------

# nums = [3, 1, 2, 2, 2, 1, 3]
# n = len(nums)
# k = 2
#
# counter = 0
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if 0 <= i < j < n:
#             if nums[i] == nums[j] and ((i * j) % k == 0):
#                 counter += 1
#
# print(counter)


# --------------------------
# Solution 1 (38ms runtime)
# --------------------------

# from typing import List  # Optional
#
#
# class Solution:
#     def countPairs(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         counter = 0
#
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if 0 <= i < j < n:
#                     if nums[i] == nums[j] and ((i * j) % k == 0):
#                         counter += 1
#         return counter


# -----------------------
# Testint 2: Optimizaion
# -----------------------

# from collections import defaultdict
#
# nums = [3, 1, 2, 2, 2, 1, 3]
# k = 2
#
# groups = defaultdict(list)
#
# for index, value in enumerate(nums):
#     groups[value].append(index)
#
# count = 0
#
# for index_list in groups.values():
#     for i in range(len(index_list)):
#         for j in range(i + 1, len(index_list)):
#             if (index_list[i] * index_list[j]) % k == 0:
#                 count += 1
#
# print(count)


# ------------------------------------
# Solution 2: Optimized (7ms runtime)
# ------------------------------------

from typing import List  # Optional
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        groups = defaultdict(list)

        for index, value in enumerate(nums):
            groups[value].append(index)

        count = 0

        for index_list in groups.values():
            for i in range(len(index_list)):
                for j in range(i + 1, len(index_list)):
                    if (index_list[i] * index_list[j]) % k == 0:
                        count += 1

        return count
