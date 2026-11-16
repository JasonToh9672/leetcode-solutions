# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Time complexity: O(n) because each node is visited once
# Space complexity: O(1) because I only use 3 variables (previous, current, next_node), no matter how long the list is
# LeetCode runtime: 0 ms


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# First attempt
# Time complexity: O(n)
# Space complexity: O(n) because the values list grows with the list
"""
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        for value in values:                # NOT reversed(values): adding to the front already flips the order
            head = ListNode(value, head)    # round 1: head is None (we walked off the end), so node 1 points at None → it becomes the LAST node
        return head                         # round 2: node 2 points at the old head (node 1) → 2 → 1. Each new node goes in front, so the order flips
"""

# -------------------------------------------------------------------------------------------------
# Second attempt
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        current = head
        while current is not None:
            next_node = current.next    # 1. bookmark the node ahead
            current.next = previous     # 2. turn current's arrow around
            previous = current          # 3. step previous forward
            current = next_node         # 4. step current forward
        return previous                 # when current is None, previous is the last node, it is on the old LAST node (3), which is the FIRST node now (3 -> 2 -> 1)


def build_linked_list(values):           # [1, 2, 3] → 1 → 2 → 3
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_python_list(head):                # 1 → 2 → 3 → [1, 2, 3]
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


if __name__ == "__main__":
    sol = Solution()
    print(to_python_list(sol.reverseList(build_linked_list([1, 2, 3]))))         # [3, 2, 1]
    print(to_python_list(sol.reverseList(build_linked_list([1, 2, 3, 4, 5]))))   # [5, 4, 3, 2, 1]
    print(to_python_list(sol.reverseList(build_linked_list([1]))))               # [1]   (one node)
    print(to_python_list(sol.reverseList(build_linked_list([]))))                # []    (empty: loop never runs)


# Trace table for 1 → 2 → 3 (fill in rounds 2 and 3; check with the stepper page)
#
# Round | next_node (bookmark) | arrow turned        | previous ends on | current ends on
# ------+----------------------+---------------------+------------------+----------------
#   1   | node 2               | 1 now points at None | node 1           | node 2
#   2   | node 3               | 2 now points at 1    | node 2           | node 3
#   3   | None                 | 3 now points at 2    | node 3           | None
#
# After round 3: current is None, so the loop stops, and previous is on node 3 (the new head).
#
#   None ← 1 ← 2 ← 3
#                  ↑
#               previous


# What I learned:
# - First attempt bug: I used reversed(values) AND added each node to the front.
#   Adding to the front already flips the order once, so flipping twice gave original.
# - Second attempt: walk once with 3 variables (previous, current, next_node). Each round has 4 steps:
#     1. Save the current's next node
#     2. Change the current's next direction to previous
#     3. Move previous one step forward, onto current
#     4. Move current one step forward, onto next_node (the bookmark)
# - The bookmark (step 1) must come BEFORE turning the arrow (step 2), because only the node has the direction to next node, if we did not save it, we lose the direction to the next node.
# - Return previous, not current or next_node: when the loop stops, current is None,
#   and previous is on node 3 (The last node of original and first node on reversed list).
# - Empty list: the loop never runs, so next_node is NEVER CREATED (it's only made inside the loop).
#   So return next_node would CRASH (UnboundLocalError), not return None.
# - Pointer problems are easier when I draw on paper first.