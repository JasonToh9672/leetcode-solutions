# 136. Single Number
# https://leetcode.com/problems/single-number/
# Time complexity: O(n)
# Space complexity: O(1)
# LeetCode runtime: 1 ms


# First attempt
# Time complexity: O(n) because I loop through nums once, then through the dict once
# Space complexity: O(n) because the dict grows with the number of different numbers
"""
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1    # count how many times each number appears
        for num, count in counts.items():           # go through each (number, count) pair
            if count == 1:                          # the one that appears only once
                return num
"""

# -----------------------------------------------------------------------------------------------------------
# Second attempt
# Time complexity: O(n) because I loop through nums once
# Space complexity: O(1) because I only use one variable (result), no matter how long the list is

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0                  # start at 0, because x ^ 0 = x (XOR with 0 changes nothing)
        for num in nums:
            result = result ^ num   # XOR every number in; each pair cancels out (x ^ x = 0)
        return result               # only the number without a partner is left  (x ^ x = 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))          # 1   (LeetCode example 1)
    print(sol.singleNumber([4, 1, 2, 1, 2]))    # 4   (LeetCode example 2)
    print(sol.singleNumber([1]))                # 1   (only one number)
    print(sol.singleNumber([1, 1, 2, 2, 3]))    # 3   (single number at the end)
    print(sol.singleNumber([-1, -1, -2]))       # -2  (negative numbers work too)


# What I learned:
# - XOR (^) compares bits: same → 0, different → 1.
#   Like a light switch: XOR with 1 = flip it, and flipping twice = back to where it started.
#
# - 3 rules:
#     x ^ x = 0     (a number cancels itself)
#     x ^ 0 = x     (XOR with 0 changes nothing, so result starts at 0)
#     the order does not matter, so the pairs cancel even when they're not next to each other
#
# - Trace for [4, 1, 2, 1, 2]:
#     step | XOR with | result
#     start|          |   0
#       1  |    4     |   4   (000 XOR 100 = 100) - 4
#       2  |    1     |   5   (100 XOR 001 = 101) - 5
#       3  |    2     |   7   (101 XOR 010 = 111) - 7
#       4  |    1     |   6   (111 XOR 001 = 110) - 6
#       5  |    2     |   4   ← the answer (110 XOR 010 = 100) - 4
#   The middle results look like different, but the pairs (1, 1) and (2, 2) cancel in the end.
#
# - First attempt (dict) uses O(n) space, because the dict grows with the input list of numbers.
#   Second attempt (XOR) uses O(1) space, because we only create one variable result.