# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Time complexity: O(n)
# Space complexity: O(n) because if input = "((((((": every character goes onto the stack, so the stack grows as big as the input.
# LeetCode runtime: 1 ms

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")",
                   "{": "}",
                   "[": "]"}

        for char in s:
            if char in mapping: # check the opening brackets, if yes, append into stack
                stack.append(char)
            elif char in mapping.values(): #check the closing brackets
                if not stack: #check if the stack is empty, if stack: True means the stack got items, if not stack: True means the stack is empty
                    return False #empty stack and no opening brackets in the stack to check with closing brackets #and the first cannot be closing brackets so straight return False 
                else:  # if stack is not empty and got opening brackets
                    top_element = stack.pop() # pop the top opening brackets and return to variable top_element, for one closing brackets, we pop one opening brackets from stack and compare
                    """
                    if char == mapping[top_element]:
                        return True             # this cannot because it straight return True when there is only one match, when after that not matching also already return True before
                    else:
                        return False
                    """
                    if char != mapping[top_element]: #do not decide True, only decide False when there is one mismatch, only all is matching and stack is empty at last only return True
                        return False
                    
        # If the stack is completely empty, it means all brackets matched up perfectly.
        return not stack # if it is not stack(empty) return True, else if still got items return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()[]{}"))   # True
    print(sol.isValid("([])"))     # True
    print(sol.isValid("(]"))       # False
    print(sol.isValid("([)]"))     # False
    print(sol.isValid("]"))        # False  (closing with empty stack)
    print(sol.isValid("(("))       # False  (never closed)
    print(sol.isValid("()]"))      # should be False

"""
So we basically put all opening brackets in the stack, and when there is a closing bracket, we do not append into stack, we just matching outside
we pop the opening brackets from stack and compare the matching, so means one closing brackets will remove one opening brackets in the stack
"""
# if [list] or if {dict} means checking if the list or dictionary is empty or not, if stack: returns True when it is NOT EMPTY, and if not stack: returns True when it is EMPTY
# .pop() will remove and return the value, while .remove() in list only remove


# What I learned:
# a stack is last in, first out: the top opening bracket must be closed first
# push opening brackets, and when I see a closing bracket, pop and compare
# inside the loop I only decide False; True is decided after the loop with return not stack