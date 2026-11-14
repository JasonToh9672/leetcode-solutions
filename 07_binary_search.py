# 704. Binary Search
# https://leetcode.com/problems/binary-search/
# Time complexity: O(log n) because each round throws away half of the numbers that are left
# Space complexity: O(1) because I only use a few variables (left, right, middle, guess), no matter how big the list is
# LeetCode runtime: 0 ms

# First attempt
# Time complexity: O(n)
# Space complexity: O(n)
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        index = {}
        for i, num in enumerate(nums):
            index[num] = i
            if target in index:
                return index[target]
        return -1
"""

#-------------------------------------------------------------------------------------------------------------------------------
# Second attempt
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right: # so when left = right still run and get that value
            middle = (right + left) // 2
            guess = nums[middle]
            if guess == target:
                return middle
            elif guess < target:  # in sorted list, we know the guess and its left are all smaller than target
                left = middle + 1 # so we start after the middle
            else:
                right = middle - 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))    # 4   (target in the right half)
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))    # -1  (not in the list)
    print(sol.search([-1, 0, 3, 5, 9, 12], -1))   # 0   (first number)
    print(sol.search([-1, 0, 3, 5, 9, 12], 12))   # 5   (last number)
    print(sol.search([5], 5))                     # 0   (one number, needs <= not <)
    print(sol.search([5], 3))                     # -1  (one number, not found)


# What I learned:
# O(log n) = each round throws away HALF of what's left. Example:
#
#   n = 16              # imagine a list of 16 numbers
#   steps = 0
#   while n > 1:        # keep going while more than 1 number is left
#       n = n // 2      # throw away half: 16 → 8 → 4 → 2 → 1
#       steps += 1      # count one round
#   print(steps)        # 4 rounds (a normal loop through 16 numbers = 16 rounds)
#
#   Binary search works the same way: each round, half of the list is thrown away.
#   1,000,000 numbers → only about 20 rounds instead of 1,000,000 rounds.
#
# "sorted" is what makes throwing half away safe: if nums[middle] is smaller than the target,
#   then the middle AND everything to its left are smaller too, so the target can't be there
# left <= right (not <): when only 1 number is left, left == right,
#   and that last number still has to be checked (e.g. nums = [5], target = 5)
# middle + 1 / middle - 1 (not middle): I've already checked the middle, so skip it;
#   using middle could make the loop repeat forever