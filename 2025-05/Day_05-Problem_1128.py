"""
1128. Number of Equivalent Domino Pairs (Easy)

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if
either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].


Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1


Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3


Constraints:
    1 <= dominoes.length <= 4 * 104
    dominoes[i].length == 2
    1 <= dominoes[i][j] <= 9


Hint 1
For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.

Hint 2
You can keep track of what you've seen using a hashmap.
"""

# -------------------------
# Testing: Using a hashmap
# -------------------------

# from collections import defaultdict
#
# dominoes = [[1, 2], [2, 1], [1, 2], [3, 4]]
# count = defaultdict(int)
# result = 0
#
# for a, b in dominoes:
#     key = tuple(sorted((a, b)))
#     result += count[key]
#     count[key] += 1
#
# print(result)


# -----------------------------------------
# Solution: Using a hashmap (16ms runtime)
# -----------------------------------------

from typing import List  # Optional
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            result += count[key]
            count[key] += 1

        return result
