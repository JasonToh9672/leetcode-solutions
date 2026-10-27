# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Time complexity: O(n)
# LeetCode runtime: 17 ms

# First attempt
# Time complexity: O(n²)
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                return True
        return False

# Submission with Time Limit Exceeded
# checking one by one in list is slow for big sets of data
"""

#-------------------------------------------------------------------------------------------------------------------------------
# Second attempt

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

"""
A set is like a dict that only has keys, with no values, it removes duplicates automatically

seen = set()        # empty set (note: {} would make an empty dict, not a set)
seen.add(5)         # sets use .add(), not .append()
seen.add(3)
seen.add(5)         # adding 5 again does nothing, since sets never hold duplicates

print(seen)         # {3, 5}
print(5 in seen)    # True, and it's instant, even with millions of items
print(9 in seen)    # False
"""

# What I learned:
# list is slow because it checks each data one by one
# set is fast because it checks the key directly like a dict
# choose set when you need to check if something exists many times (e.g. finding duplicates)