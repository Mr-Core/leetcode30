"""
3392. Count Subarrays of Length Three With a Condition (Easy)

Given an integer array nums, return the number of subarray of length 3 such that the
sum of the first and third numbers equals exactly half of the second number.


Example 1:

Input: nums = [1,2,1,4,1]
Output: 1

Explanation:
Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.


Example 2:

Input: nums = [1,1,1]
Output: 0

Explanation:
[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.


Constraints:
    3 <= nums.length <= 100
    -100 <= nums[i] <= 100


Hint 1
The constraints are small. Consider checking every subarray.
"""

# ------------------------
# Testing 1: Using slices
# ------------------------

# nums = [1, 2, 1, 4, 1]
# n = len(nums)
# result = 0
#
# for i in range(n - 2):
#     test = nums[i : i + 3]
#     if test[0] + test[2] == test[1] // 2:
#         result += 1
#
# print(result)


# ---------------------------------------
# Solution 1: Using slice (15ms runtime)
# ---------------------------------------

# from typing import List  # Optional
#
#
# class Solution:
#     def countSubarrays(self, nums: List[int]) -> int:
#         n = len(nums)
#         result = 0
#
#         for i in range(n - 2):
#             test = nums[i : i + 3]
#             if test[0] + test[2] == test[1] / 2:
#                 result += 1
#
#         return result


# ---------------------------
# Testing 2: Direct indexing
# ---------------------------

# nums = [1, 2, 1, 4, 1]
# n = len(nums)
# result = 0
#
# for i in range(n - 2):
#     if nums[i] + nums[i + 2] == nums[i + 1] / 2:
#         result += 1
#
# print(result)


# ------------------------------------------
# Solution 2: Direct indexing (7ms runtime)
# ------------------------------------------

from typing import List  # Optional


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n - 2):
            if nums[i] + nums[i + 2] == nums[i + 1] / 2:
                result += 1

        return result
