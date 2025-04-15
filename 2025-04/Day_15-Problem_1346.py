"""
1346. Check If N and Its Double Exist (Easy)

Given an array arr of integers, check if there exist two indices i and j such that :
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]


Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]


Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.


Constraints:
    2 <= arr.length <= 500
    -103 <= arr[i] <= 103


Hint 1
Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].

Hint 2
On each step of the loop check if we have seen the element 2 * arr[i] so far.

Hint 3
Also check if we have seen arr[i] / 2 in case arr[i] % 2 == 0.
"""

# -----------------------
# Testing 1: Brute force
# -----------------------

# arr = [10, 2, 5, 3]
#
# output = False
#
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i != j:
#             if arr[i] == 2 * arr[j]:
#                 output = True
#
#     if output:
#         break
#
# print(output)


# ---------------------------------------
# Solution 1: Brute force (10ms runtime)
# ---------------------------------------

# from typing import List  # Optional
#
#
# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         output = False
#
#         for i in range(len(arr)):
#             for j in range(len(arr)):
#                 if i != j:
#                     if arr[i] == 2 * arr[j]:
#                         output = True
#
#             if output:
#                 break
#
#         return output


# ------------------------------------
# Testing 2: Set and Hash Table logic
# ------------------------------------

# arr = [10, 2, 5, 3]
# seen = set()
# output = False
#
# for num in arr:
#     if (2 * num in seen) or (num % 2 == 0 and num // 2 in seen):
#         output = True
#     seen.add(num)
#
# print(output)


# ---------------------------------------------------
# Solution 2: Set and Hash Table logic (0ms runtime)
# ---------------------------------------------------

from typing import List  # Optional


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        output = False

        for num in arr:
            if (2 * num in seen) or (num % 2 == 0 and num // 2 in seen):
                output = True
            seen.add(num)

        return output
