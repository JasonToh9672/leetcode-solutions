# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Time complexity: O(n)
# LeetCode runtime: 0 ms

# First attempt
# Time complexity: O(n²), 1779 ms

"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output = [i, j]
                    return output
"""

#-------------------------------------------------------------------------------------------------------------------------------
# Second attempt

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            partner = target - num
            if partner in seen: # check first before insert
                return [seen[partner], i]
            seen[num] = i

# What I learned:
# the partner trick: partner = target - num
# the hash map lookup pattern: store what you’ve seen in a dict, then check instantly instead of looping again

# enumerate produce index and value and can change start position
# enumerate(iterable, start=0)
# start= only changes the counter, not the real positions in the list, so don’t use it when you need real indices.

# we need to check first before insert because for example nums = [1,2,3,4], target = 6
# if we insert before check, when i=2, num=3, partner=3, it will insert 3 into the dict then check if the taget inside
# since it's inserted before, so it directly return two same indices
