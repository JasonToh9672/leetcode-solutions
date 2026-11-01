# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Time complexity: O(n)
# Space complexity: O(1)
# LeetCode runtime: 8 ms

# First attempt
# Time complexity: O(n), 5 ms
# Space complexity: O(n), the alphanum holds same number of characters with input s
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        alphanum = ""
        for char in lower_s:
            if char.isalnum():  #.isalnum() check is the string is alphanumerical and return True or False
                alphanum += char

        return alphanum == alphanum[::-1] # [:] means from beginning to end with default 1 step, [::-1] means from the end to beginning with -1 step (reverse) 
"""

#-------------------------------------------------------------------------------------------------------------------------------
# Second attempt
# Time complexity: O(n), 8ms
# Space complexity: O(1), we did not store any variable that is increasing along the input, instead we use pointer to check left and right

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum(): # if dont add while left < right here it will crash. When "?/-" has length 3, so its valid indices are 0, 1, 2. 
                left += 1                                 # Without the guard, left keeps increasing until it reaches 3, and s[3] crashes with an IndexError because index 3 doesn’t exist.
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters directly (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False # if any left and right not match, straight return False as they are not Palindrome, no need continue

            left += 1
            right -= 1
        return True

# What I learned:
# two pointers: start one at the beginning and one at the end of the string, then move them toward the middle step by step
# the inner while loops need left < right because without the guard, if a string has no letters or numbers (like "?/-"),
#   left keeps increasing past the last index and crashes with an IndexError
# my O(1) version was slower on LeetCode because my while loop runs in Python, while .lower() and [::-1] run in fast built-in code,
#   but the space improvement (O(n) → O(1)) matters more in interviews

"""
The tool: .isalnum()

Strings have a method called .isalnum(). It answers: “Is every character in this string a letter or a number?” It returns True or False.

Try it on single characters:

python
print("a".isalnum())   # True  (letter)
print("Z".isalnum())   # True  (letter)
print("7".isalnum())   # True  (number)
print(",".isalnum())   # False (punctuation)
print(" ".isalnum())   # False (space)
print(":".isalnum())   # False

The name means is alphanumeric: “alpha” for letters, “numeric” for numbers.
"""

"""
A full slice looks like this: [start:stop:step] # the step matters to decide it is move forward or backward

If you leave any of these positions empty (just using the colon : ), Python falls back to these defaults:
• Blank start = Start at index 0 (the very beginning).
• Blank stop = Go all the way to the end of the sequence.
• Blank step = Move forward by 1 element at a time.


Common Examples of What : Means

• [:] (The Single Colon): This means "start at the beginning and go all the way to the end." It creates a shallow copy of the entire sequence.
my_list = [1, 2, 3]
print(my_list[:])  # Output: [1, 2, 3]

• [:3] (Blank Start): This means "start at the beginning and stop before index 3."
my_list = ['a', 'b', 'c', 'd']
print(my_list[:3])  # Output: ['a', 'b', 'c']

• [2:] (Blank Stop): This means "start at index 2 and go all the way to the end."
my_list = ['a', 'b', 'c', 'd']
print(my_list[2:])  # Output: ['c', 'd']

• [::-1] (Blank Start and Stop): This means "go from the beginning to the end, but move backward by 1." (Reverses it).
my_list = [1, 2, 3]
print(my_list[::-1])  # Output: [3, 2, 1]
"""

"""
When you write a slice like [ : ], the colon acts as a separator, and the spaces around it are left blank.
Think of it like a fill-in-the-blank form where the default answers are already filled out for you:
• [ blank : ] → Python fills the blank with the start (index 0).
• [ : blank ] → Python fills the blank with the end (the last item).
• [ blank : blank ] → Python fills both blanks, meaning "from start to end."

Visualizing the Blanks

my_list = ['a', 'b', 'c', 'd']

# What you type:      [  : 2]   (left side is blank)
# What Python sees:   [0 : 2]   (starts at 0)

# What you type:      [2 :  ]   (right side is blank)
# What Python sees:   [2 : 4]   (goes all the way to the end)

# What you type:      [  :  ]   (both sides are blank)
# What Python sees:   [0 : 4]   (grabs the whole list)


How :: Works in Practice

Because start and stop are blank, Python automatically selects the entire sequence, and then applies your step rule:
• [::2] (Every second item): Starts at the beginning, goes to the end, but takes steps of 2 (skips every other item).
• [::3] (Every third item): Starts at the beginning, goes to the end, but takes steps of 3.
• [::-1] (Reverse everything): Starts at the end, goes to the beginning, taking steps of -1 (moves backward).

Code Examples

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. Skip every other item (even indices)
print(numbers[::2])  
# Output: [0, 2, 4, 6, 8]

# 2. Grab every third item
print(numbers[::3])  
# Output: [0, 3, 6, 9]

# 3. Flip the whole thing backward
print(numbers[::-1])  
# Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

[::-1] is same with [-1::-1]

Quick Comparison

letters = ['a', 'b', 'c', 'd']

print(letters[::-1])     # Output: ['d', 'c', 'b', 'a'] (Blanks handle boundaries perfectly)
print(letters[-1::-1])   # Output: ['d', 'c', 'b', 'a'] (Explicit start, blank stop)
print(letters[-1:0:-1])  # Output: ['d', 'c', 'b']      (Excludes index 0!)

"""