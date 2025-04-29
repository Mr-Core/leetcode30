"""
2962. Count Subarrays Where Max Element Appears at Least K Times (Medium)

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.


Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].


Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.


Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 106
    1 <= k <= 105
"""

# ---------------------------
# Testint 1: Brute (of)force
# ---------------------------

# from collections import defaultdict
#
# nums = [3, 3, 3]
# k = 2
#
# mx = max(nums)
# count = 0
# n = len(nums)
#
# for start in range(n):
#     freq_max = 0
#     for end in range(start, n):
#         if nums[end] == mx:
#             freq_max += 1
#         # only count if the global max has appeared ≥ k times
#         if freq_max >= k:
#             count += 1
#
# print(count)


# ----------------------------------------------
# Solution 1: Brute force (Time Limit Exceeded)
# ----------------------------------------------

# from typing import List  # Optional
# from collections import defaultdict
#
#
# def count_good_subarrays(nums, k):
#     mx = max(nums)
#     count = 0
#     n = len(nums)
#
#     for start in range(n):
#         freq_max = 0
#         for end in range(start, n):
#             if nums[end] == mx:
#                 freq_max += 1
#             if freq_max >= k:
#                 count += 1
#
#     return count


# ----------------------------------------
# Testint 2: Sliding-window (two-pointer)
# ----------------------------------------

# nums = [3, 3, 3]
# k = 2

# maximum = max(nums)  # global maximum of the array
# n = len(nums)
# l = 0
# count = 0  # how many times mx appears in current window
# output = 0

# for r in range(n):
#     if nums[r] == maximum:
#         count += 1

#     # As soon as we have at least k occurrences, we can
#     # move l forward to make the window just barely invalid
#     # (i.e. cnt == k-1), counting all those valid subarrays.
#     while count >= k:
#         if nums[l] == maximum:
#             count -= 1
#         l += 1

#     # Now, all subarrays ending at r and starting at any index
#     # in [0, l-1] are valid (because if l moved to the first
#     # position that broke the condition, then [0..l-1] all have
#     # at least k occurrences of mx).
#     output += l

# print(output)


# -------------------------------------------------------
# Solution 2: Sliding-window (two-pointer) (67ms runtime)
# -------------------------------------------------------

from typing import List  # Optional


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        n = len(nums)
        l = 0
        count = 0
        output = 0

        for r in range(n):
            if nums[r] == maximum:
                count += 1

            while count >= k:
                if nums[l] == maximum:
                    count -= 1
                l += 1

            output += l

        return output
