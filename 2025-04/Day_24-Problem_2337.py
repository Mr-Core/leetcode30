"""
2337. Move Pieces to Obtain a String (Medium)

You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:
    The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
    The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.

Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.


Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.


Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.


Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.


Constraints:
    n == start.length == target.length
    1 <= n <= 105
    start and target consist of the characters 'L', 'R', and '_'.


Hint 1
After some sequence of moves, can the order of the pieces change?

Hint 2
Try to match each piece in s with a piece in e.
"""

# ----------------------------
# Testing 1: with defaultdict
# ----------------------------

# from collections import defaultdict
#
# start = "_L__R__R_"
# target = "L______RR"
#
# start_indexes = defaultdict(list)
# target_indexes = defaultdict(list)
#
# if start.replace("_", "") != target.replace("_", ""):
#     print("False")
# else:
#     for index, char in enumerate(start):
#         if char in "LR":
#             start_indexes[char].append(index)
#
#     for index, char in enumerate(target):
#         if char in "LR":
#             target_indexes[char].append(index)
#
#     for piece in "LR":
#         for s_idx, t_idx in zip(start_indexes[piece], target_indexes[piece]):
#             if piece == "L" and s_idx < t_idx:
#                 print("False")
#             elif piece == "R" and s_idx > t_idx:
#                 print("False")
#
#     print("True")


# ---------------------------------------------
# Solution 1: with defaultdict (126ms runtime)
# ---------------------------------------------

from collections import defaultdict


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_indexes = defaultdict(list)
        target_indexes = defaultdict(list)

        if start.replace("_", "") != target.replace("_", ""):
            return False

        for index, char in enumerate(start):
            if char in "LR":
                start_indexes[char].append(index)

        for index, char in enumerate(target):
            if char in "LR":
                target_indexes[char].append(index)

        for piece in "LR":
            for s_idx, t_idx in zip(start_indexes[piece], target_indexes[piece]):
                if piece == "L" and s_idx < t_idx:
                    return False
                elif piece == "R" and s_idx > t_idx:
                    return False

        return True


# -----------------------------
# Testing 2: using plain lists
# -----------------------------

# start = "_L__R__R_"
# target = "L______RR"
#
# start_L = []
# start_R = []
# target_L = []
# target_R = []
#
# if start.replace("_", "") != target.replace("_", ""):
#     print("False")
# else:
#     for i in range(len(start)):
#         if start[i] == "L":
#             start_L.append(i)
#         elif start[i] == "R":
#             start_R.append(i)
#
#         if target[i] == "L":
#             target_L.append(i)
#         elif target[i] == "R":
#             target_R.append(i)
#
#     for s_idx, t_idx in zip(start_L, target_L):
#         if s_idx < t_idx:
#             print("False")
#
#     for s_idx, t_idx in zip(start_R, target_R):
#         if s_idx > t_idx:
#             print("False")
#
#     print("True")


# ----------------------------------------------
# Solution 2: using plain lists (133ms runtime)
# ----------------------------------------------


# class Solution:
#     def canChange(self, start: str, target: str) -> bool:
#         if start.replace("_", "") != target.replace("_", ""):
#             return False
#
#         start_L = []
#         start_R = []
#         target_L = []
#         target_R = []
#
#         for i in range(len(start)):
#             if start[i] == "L":
#                 start_L.append(i)
#             elif start[i] == "R":
#                 start_R.append(i)
#
#             if target[i] == "L":
#                 target_L.append(i)
#             elif target[i] == "R":
#                 target_R.append(i)
#
#         for s_idx, t_idx in zip(start_L, target_L):
#             if s_idx < t_idx:
#                 return False
#
#         for s_idx, t_idx in zip(start_R, target_R):
#             if s_idx > t_idx:
#                 return False
#
#         return True
