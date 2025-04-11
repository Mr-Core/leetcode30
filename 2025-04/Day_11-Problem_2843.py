"""
2843. Count Symmetric Integers (Easy)

You are given two positive integers low and high.
An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x.
Numbers with an odd number of digits are never symmetric.
Return the number of symmetric integers in the range [low, high].


Example 1:

Input: low = 1, high = 100
Output: 9
Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.


Example 2:

Input: low = 1200, high = 1230
Output: 4
Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.


Constraints:
    1 <= low <= high <= 104


Hint 1
Iterate over all numbers from low to high.

Hint 2
Convert each number to a string and compare the sum of the first half with that of the second.
"""

# -------------------
# Testing: 1st draft
# -------------------

# low = 1
# high = 100
#
# results = []
# counter = 0
#
# for n in range(low, high + 1):
#     n_string = str(n)
#
#     if (len(n_string) % 2) != 0:
#         pass
#
#     else:
#         first_part = n_string[: len(n_string) // 2]
#         second_part = n_string[len(n_string) // 2 :]
#
#         if (len(first_part) % 2) == 0:
#             first_sum_one = first_part[: len(first_part) // 2]
#             first_sum_two = first_part[len(first_part) // 2 :]
#
#             first_sum_final = int(first_sum_one) + int(first_sum_two)
#         else:
#             first_sum_final = first_part
#
#         if (len(second_part) % 2) == 0:
#             second_sum_one = second_part[: len(second_part) // 2]
#             second_sum_two = second_part[len(second_part) // 2 :]
#
#             second_sum_final = int(second_sum_one) + int(second_sum_two)
#         else:
#             second_sum_final = second_part
#
#         if first_sum_final == second_sum_final:
#             results.append(n)
#             counter += 1
#
# print(f"There are {counter} symmetric integers between {low} and {high}: {results}")


# -----------------------------
# 1st solution: from 1st draft
# -----------------------------

# counter = 0
#
# for n in range(low, high + 1):
#     n_string = str(n)
#
#     if (len(n_string) % 2) != 0:
#         pass
#
#     else:
#         first_part = n_string[: len(n_string) // 2]
#         second_part = n_string[len(n_string) // 2 :]
#
#         if (len(first_part) % 2) == 0:
#             first_sum_one = first_part[: len(first_part) // 2]
#             first_sum_two = first_part[len(first_part) // 2 :]
#
#             first_sum_final = int(first_sum_one) + int(first_sum_two)
#         else:
#             first_sum_final = first_part
#
#         if (len(second_part) % 2) == 0:
#             second_sum_one = second_part[: len(second_part) // 2]
#             second_sum_two = second_part[len(second_part) // 2 :]
#
#             second_sum_final = int(second_sum_one) + int(second_sum_two)
#         else:
#             second_sum_final = second_part
#
#         if first_sum_final == second_sum_final:
#             counter += 1
#
# return counter


# -------------------------------------------
# Testing: 2nd draft (optimized, but slower)
# -------------------------------------------

# low = 1
# high = 100
#
# results = []
# counter = 0
#
# for n in range(low, high + 1):
#     s = str(n)
#
#     if len(s) % 2 != 0:
#         continue
#
#     half = len(s) // 2
#     left = s[:half]
#     right = s[half:]
#
#     left_sum = sum(int(digit) for digit in left)
#     right_sum = sum(int(digit) for digit in right)
#
#     if left_sum == right_sum:
#         results.append(n)
#         counter += 1
#
# print(f"There are {counter} symmetric integers between {low} and {high}: {results}")


# -----------------------------
# 2nd solution: from 2nd draft
# -----------------------------

# counter = 0
#
# for n in range(low, high + 1):
#     s = str(n)
#
#     if len(s) % 2 != 0:
#         continue
#
#     half = len(s) // 2
#     left = s[:half]
#     right = s[half:]
#
#     left_sum = sum(int(digit) for digit in left)
#     right_sum = sum(int(digit) for digit in right)
#
#     if left_sum == right_sum:
#         counter += 1
#
# return counter


# Interesting note:
# 1st solution runtime: 631 ms
# 2nd solution runtime: 825 ms
