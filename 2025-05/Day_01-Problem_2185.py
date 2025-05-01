"""
2185. Counting Words With a Given Prefix (Easy)

You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.


Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".


Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.


Constraints:
    1 <= words.length <= 100
    1 <= words[i].length, pref.length <= 100
    words[i] and pref consist of lowercase English letters.


Hint 1
Go through each word in words and increment the answer if pref is a prefix of the word.
"""

# --------
# Testing
# --------

# words = ["pay", "attention", "practice", "attend"]
# pref = "at"
# n = len(pref)
# count = 0
#
# for word in words:
#     if pref in word[:n]:  # or: if word.startswith(pref):
#
#         count += 1
#
# print(count)


# -----------------------
# Solution (0ms runtime)
# -----------------------

from typing import List  # Optional


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0

        for word in words:
            if pref in word[:n]:  # or: if word.startswith(pref):
                count += 1

        return count
