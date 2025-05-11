"""
1550. Three Consecutive Odds (Easy)

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.


Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.


Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.


Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000


Hint 1
Check every three consecutive numbers in the array for parity.
"""

# --------
# Testing
# --------

# from typing import List  # Optional
#
#
# def threeConsecutiveOdds(arr: List[int]) -> bool:
#     for i in range(len(arr) - 2):
#         test = [arr[i], arr[i + 1], arr[i + 2]]
#
#         if test[0] % 2 != 0 and test[1] % 2 != 0 and test[2] % 2 != 0:
#             return True
#
#     return False
#
#
# arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
# print(threeConsecutiveOdds(arr))


# -----------------------
# Solution (0ms runtime)
# -----------------------

from typing import List  # Optional


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            test = [arr[i], arr[i + 1], arr[i + 2]]

            if test[0] % 2 != 0 and test[1] % 2 != 0 and test[2] % 2 != 0:
                return True

        return False
