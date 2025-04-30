"""
1295. Find Numbers with Even Number of Digits (Easy)

Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.


Example 2:

Input: nums = [555,901,482,1771]
Output: 1
Explanation:
Only 1771 contains an even number of digits.


Constraints:
    1 <= nums.length <= 500
    1 <= nums[i] <= 105


Hint 1
How to compute the number of digits of a number ?

Hint 2
Divide the number by 10 again and again to get the number of digits.
"""

# -----------------------------
# Testing 1: String conversion
# -----------------------------

# nums = [12, 345, 2, 6, 7896]
# n = len(nums)
# even_count = 0
#
# for i in range(n):
#     if len(str(nums[i])) % 2 == 0:
#         even_count += 1
#
# print(even_count)


# --------------------------------------------
# Solution 1: String conversion (0ms runtime)
# --------------------------------------------

from typing import List  # Optional


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        even_count = 0

        for i in range(n):
            if len(str(nums[i])) % 2 == 0:
                even_count += 1

        return even_count


# ------------------------
# Testing 2: Using modulo
# ------------------------

# nums = [12, 345, 2, 6, 7896]
# even_count = 0
#
# for num in nums:
#     digits = 0
#
#     while num > 0:
#         num //= 10
#         digits += 1
#
#     if digits % 2 == 0:
#         even_count += 1
#
# print(even_count)


# ---------------------------------------
# Solution 2: Using modulo (3ms runtime)
# ---------------------------------------

# from typing import List  # Optional
#
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         even_count = 0
#
#         for num in nums:
#             digits = 0
#
#             while num > 0:
#                 num //= 10
#                 digits += 1
#
#             if digits % 2 == 0:
#                 even_count += 1
#
#         return even_count
