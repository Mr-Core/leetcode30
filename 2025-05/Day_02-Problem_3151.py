"""
3151. Special Array I (Easy)

An array is considered special if the parity of every pair of adjacent elements is different.
In other words, one element in each pair must be even, and the other must be odd.
You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.


Example 1:
Input: nums = [1]
Output: true

Explanation:
There is only one element. So the answer is true.


Example 2:
Input: nums = [2,1,4]
Output: true

Explanation:
There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.


Example 3:
Input: nums = [4,3,1,6]
Output: false

Explanation:
nums[1] and nums[2] are both odd. So the answer is false.


Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 100


Hint 1
Try to check the parity of each element and its previous element.


Comment:
Just remember:
-> odd number + even number = odd number
-> even number + even number = even number
-> odd number + odd number = even number
Just apply the logic and you are done!
"""

# ---------------------------
# Testing 1: long way around
# ---------------------------

# nums = [4, 3, 1, 6]
# n = len(nums)
# pairs = []
# output = True
#
# if n == 1:
#     print("Only 1 number, return True")
#
# for i in range(n - 1):
#     pairs.append((nums[i], nums[i + 1]))
#
# for pair in pairs:
#     if pair[0] % 2 != 0 and pair[1] % 2 != 0:
#         output = False
#
# print(output)


# ----------
# Testing 2
# ----------

# from typing import List  # Optional
#
# def isArraySpecial(nums: List[int]) -> bool:
#     for i in range(len(nums) - 1):
#         if nums[i] % 2 == nums[i + 1] % 2:
#             return False
#     return True
#
#
# nums = [2, 1, 4]
# print(isArraySpecial(nums))


# -----------------------
# Solution (0ms runtime)
# -----------------------

from typing import List  # Optional


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
