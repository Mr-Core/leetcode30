"""
1922. Count Good Numbers (Medium)

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
    For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime.
    However, "3245" is not good because 3 is at an even index but is not even.

Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 10^9 + 7.
A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.


Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".


Example 2:

Input: n = 4
Output: 400


Example 3:

Input: n = 50
Output: 564908303


Constraints:
    1 <= n <= 1015


Hint 1
Is there a formula we can use to find the count of all the good numbers?

Hint 2
Exponentiation can be done very fast if we looked at the binary bits of n.
"""

# --------
# Testing
# --------


# n = 4
# MOD = 10**9 + 7
#
# even_positions = (n + 1) // 2  # even indices: 0, 2, 4, ...
# odd_positions = n // 2  # odd indices: 1, 3, 5, ...
#
# print(f"Total length: {n}\n")
# print(f"Even positions: {even_positions} → 5 choices (even digits: 0, 2, 4, 6, 8)")
# print(f"Odd positions: {odd_positions} → 4 choices (prime digits: 2, 3, 5, 7)\n")
#
# even_part = pow(5, even_positions, MOD)
# odd_part = pow(4, odd_positions, MOD)
#
# print(f"5^{even_positions} % {MOD} = {even_part}")
# print(f"4^{odd_positions} % {MOD} = {odd_part}\n")
#
# result = (even_part * odd_part) % MOD
# print(f"Final result: ({even_part} * {odd_part}) % {MOD} = {result}")


# ---------------
# Final solution
# ---------------


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2
        odd_positions = n // 2

        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD
