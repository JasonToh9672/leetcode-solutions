# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Time complexity: O(n)
# LeetCode runtime: 10 ms

# First attempt
# Time complexity: O(n log n), 17 ms
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t) # this is already True or False
                                      # sorted always return a list
"""

#-------------------------------------------------------------------------------------------------------------------------------
# Second attempt

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = {}
        t_counts = {}
        for ch in s:
            s_counts[ch] = s_counts.get(ch, 0) + 1
        for ch in t:
            t_counts[ch] = t_counts.get(ch, 0) + 1
        return s_counts == t_counts


# What I learned:
# check simple conditions first (like different lengths) to return early and skip extra work
# an anagram means the same letter counts, so a counting dict solves it

# return a == b  does the same as:
#   if a == b: return True
#   else: return False
# because a == b already gives True or False