"""
1534. Count Good Triplets (Easy)

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.
Return the number of good triplets.


Example 1:

Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].


Example 2:

Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.


Constraints:
    3 <= arr.length <= 100
    0 <= arr[i] <= 1000
    0 <= a, b, c <= 1000


Hint 1
Notice that the constraints are small enough for a brute force solution to pass.

Hint 2
Loop through all triplets, and count the ones that are good.
"""

# --------
# Testing
# --------


# arr = [3, 0, 1, 1, 9, 7]
# a = 7
# b = 2
# c = 3
#
# count = 0
# n = len(arr)
#
# for i in range(n):
#     for j in range(i + 1, n):
#         if abs(arr[i] - arr[j]) <= a:
#             for k in range(j + 1, n):
#                 if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
#                     count += 1
#
# print(count)


# ---------------
# Final solution
# ---------------


from typing import List  # Optional


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
        return count
