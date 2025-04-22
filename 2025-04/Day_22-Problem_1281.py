"""
1281. Subtract the Product and Sum of Digits of an Integer (Easy)

Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15


Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21


Constraints:
    1 <= n <= 10^5


Hint 1
How to compute all digits of the number ?

Hint 2
Use modulus operator (%) to compute the last digit.

Hint 3
Generalise modulus operator idea to compute all digits.
"""

# --------
# Testing
# --------

# n = 234
# product_of_digits = 1
# sum_of_digits = 0
#
# while n > 0:
#     digit = n % 10
#     product_of_digits *= digit
#     sum_of_digits += digit
#     n //= 10
#
# result = product_of_digits - sum_of_digits
#
# print(result)


# -----------------------
# Solution (0ms runtime)
# -----------------------


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_digits = 1
        sum_of_digits = 0

        while n > 0:
            digit = n % 10
            product_of_digits *= digit
            sum_of_digits += digit
            n //= 10

        return product_of_digits - sum_of_digits
