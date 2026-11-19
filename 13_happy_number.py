# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# Time complexity: O(log n) because each step only looks at the digits of n (log n ≈ the number of digits), and the numbers shrink quickly
# Space complexity: O(log n) because the set stores the numbers seen, and there are only a few of them
# LeetCode runtime: 2 ms


def next_number(n):
    total = 0
    for ch in str(n):                # turn n into a string, so I can go through it one digit at a time
        total += int(ch) ** 2        # turn the digit back into an integer, square it, and add it to the total
    return total                     # e.g. 19 → 1² + 9² = 82


# First attempt
# Time complexity: O(log n)
# Space complexity: O(log n)
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()                 # the numbers I've already visited (a set: "x in seen" is O(1), a list would be O(n))
        while n not in seen:         # stop if a number comes back → it's going round in a loop
            seen.add(n)              # remember this number
            n = next_number(n)       # move to the next number (like current = current.next in 141)
            if n == 1:               # reached 1 → happy
                return True
        return False                 # a number came back without reaching 1 → it loops forever → not happy


if __name__ == "__main__":
    print(next_number(19))           # 82
    print(next_number(82))           # 68
    print(next_number(100))          # 1

    sol = Solution()
    print(sol.isHappy(19))           # True   (LeetCode example 1: 19 → 82 → 68 → 100 → 1)
    print(sol.isHappy(2))            # False  (LeetCode example 2: 2 → 4 → 16 → ... → 4 loops)
    print(sol.isHappy(1))            # True   (already 1)
    print(sol.isHappy(7))            # True   (7 → 49 → 97 → 130 → 10 → 1)


# What I learned:
# - A happy number reaches 1. A number that isn't happy goes round in a loop forever,
#   e.g. 2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 (back again).
#
# - It's the same idea as 141 Linked List Cycle:
#     141 Linked List Cycle            | 202 Happy Number
#     ---------------------------------+----------------------------------
#     a node                           | a number
#     current = current.next           | n = next_number(n)
#     None = the end (no cycle)        | 1 = the end (happy)
#     a node comes back = cycle        | a number comes back = not happy
#
# - I can store the NUMBERS in the set here (in 141 I had to store nodes), because the same number
#   always leads to the same next number.
#
# - Splitting out a helper (next_number) helped, because my first try wrote the digit code twice
#   and got it wrong inside the loop. Test the helper on its own first.
#
# - Don't use sum as a variable name: it's a built-in Python function.
#
# - Big-O:
#   First: what is n? n is the INPUT PARAMETER (isHappy(self, n: int)). Here it's a number,
#   so n means the number's VALUE (like one million), not a list of n items.
#   The loop is: for ch in str(n). str(n) turns the number into text, e.g. str(1000000) = '1000000'.
#   The loop goes through that text one CHARACTER (= one digit) at a time, so the work = the number of digits:
#     n (the value)    | str(n)            | steps (= digits)
#     9                | '9'               | 1
#     999              | '999'             | 3
#     1,000,000        | '1000000'         | 7        ← 7 steps, NOT one million steps
#     2,147,483,647    | '2147483647'      | 10
#   The number of digits is tiny compared with n. That's the "log n".
#
#   Example: n = 50 (the input). str(50) = '50' has 2 digits, so the loop runs 2 rounds, not 50.
#
#   Careful: "fewer rounds than n" alone doesn't mean O(log n). What matters is HOW you get fewer:
#     halve ONCE, then walk the half one by one:  16 → 8 items → 8 rounds    → O(n)
#     halve EVERY round (binary search, digits):  16 → 8 → 4 → 2 → 1 = 4    → O(log n)
#
#     n            | halve once, then walk | halve every round
#     16           | 8                     | 4
#     1,000        | 500                   | about 10
#     1,000,000    | 500,000               | about 20
#   Halve once: n × 10 → rounds × 10 → O(n).  Halve every round: n × 1,000 → only ~10 more rounds → O(log n).
#
#   The numbers also shrink fast: a 10-digit number gives at most 10 × 81 = 810 after one step,
#   so there are only a few rounds of the while loop too.