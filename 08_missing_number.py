# 268. Missing Number
# https://leetcode.com/problems/missing-number/
# Time complexity: O(n) 
# Space complexity: O(1)
# LeetCode runtime: 0 ms

# First attempt
# Time complexity: O(n)
# Space complexity: O(1)
"""
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        total = 0
        for i in range(len(nums) + 1): 
            total += i
        return total - sum(nums) 
"""

# Second attempt
# Time complexity: O(n)
# Space complexity: O(1) 
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2 # famous formula for adding up 0 + 1 + 2 + ... + n
        return total - sum(nums) 

if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([0, 1, 4, 2, 5]))                 # 3   (missing in the middle)
    print(sol.missingNumber([3, 0, 1]))                       # 2   (LeetCode example 1)
    print(sol.missingNumber([0, 1]))                          # 2   (the last number n is missing)
    print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))     # 8   (LeetCode example 3)
    print(sol.missingNumber([1]))                             # 0   (0 is missing)

# What I learned:
# - The list should have every number from 0 to n, but one is missing.
# - total = the sum of the FULL set (0 + 1 + ... + n).
#   sum(nums) = the sum of my list, which is the full set MINUS missing number.
#   So total - sum(nums) = missing number, because every other number is same.
# - Formula: 0 + 1 + ... + n = n * (n + 1) // 2.
#   Why (example n = 4): write 1..n forwards, and again backwards underneath:
#
#       row A:   1   2   3   4
#       row B:   4   3   2   1
#                -   -   -   -
#                5   5   5   5     <- every column = first + last = n + 1
#
#   Every column is the same, because row A goes up by 1 while row B goes down by 1.
#   There are 4 columns (n), each worth 5 (n + 1), so both rows = 4 * 5 = 20.
#   One row is half of that: 20 // 2 = 10.   Check: 1 + 2 + 3 + 4 = 10