# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Time complexity: O(n)
# Space complexity: O(1)
# LeetCode runtime: 52 ms

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_cycle_list(values, pos):
    nodes = []                                # keep every node in a Python list, so I can find node number "pos" later
    for value in values:
        nodes.append(ListNode(value))
    for i in range(len(nodes) - 1):           # link each node to the next one: 0 → 1 → 2 → 3. The loop uses nodes[i + 1], and the last node has no node after it,
        nodes[i].next = nodes[i + 1]          # so if i reached the last index, nodes[i + 1] would be out of range → IndexError. So we stop one early.
    if pos != -1:
        nodes[-1].next = nodes[pos]           # the LAST node points back at node number "pos" (this makes the cycle)
    if len(nodes) == 0:
        return None                           # empty list
    return nodes[0]                           # the head


# First attempt
# Time complexity: O(n)
# Space complexity: O(n) because the set grows with the number of nodes
"""
class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        current = head
        seen = set()                # the NODES I've already visited (nodes, not values: values can repeat without a cycle)
        while current is not None:  # walk through each node
            if current in seen:     # I've been in this exact node before → I'm going in circles
                return True
            seen.add(current)       # first visit: remember this node
            current = current.next
        return False                # reached None → the list ends → no cycle
"""

# -----------------------------------------------------------------------------------------------------------
# Second attempt
# Time complexity: O(n)
# Space complexity: O(1) because I only use 2 variables (slow, fast), no matter how long the list is
class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:   # fast moves 2 steps, so BOTH must exist (else None.next crashes)
            slow = slow.next          # slow moves 1 step
            fast = fast.next.next     # fast moves 2 steps
            if slow is fast:          # check AFTER moving (at the start both are on the head); "is" = the same node
                return True
        return False                  # fast reached the end → the list ends → no cycle


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasCycle(build_cycle_list([3, 2, 0, -4], 1)))   # True   (LeetCode example 1)
    print(sol.hasCycle(build_cycle_list([1, 2], 0)))          # True   (the last node points back at the first)
    print(sol.hasCycle(build_cycle_list([1], -1)))            # False  (one node, no cycle)
    print(sol.hasCycle(build_cycle_list([], -1)))             # False  (empty list)
    print(sol.hasCycle(build_cycle_list([1, 2, 3], -1)))      # False  (odd length, no cycle)
    print(sol.hasCycle(build_cycle_list([1, 1, 1], -1)))      # False  (repeated values, but no cycle)


# What I learned:
# - A cycle = the last node points back to an earlier node instead of None,
#   so the normal walk (while current is not None) would loop forever.
#
# - First attempt: store the nodes in a set, not the node value, because values can repeat without a cycle
#   (e.g. 1 → 1 → 1 → None). Space is O(n) because the set stores every node I visit, so it grows with the number of nodes.
#
# - Second attempt (fast and slow): slow moves 1 step, fast moves 2 steps.
#   If there's a cycle, fast can't escape the circle, so it catches up slow from behind.
#   They MUST meet, because each round the gap gets 1 step smaller (it can't jump over).
#
#   Trace for [3, 2, 0, -4], pos = 1:
#     round | slow | fast
#     start |  3   |  3
#       1   |  2   |  0
#       2   |  0   |  2
#       3   | -4   | -4   ← same node → True
#
# - The loop needs BOTH checks, because fast moves 2 steps:
#     list (no cycle)     | where fast ends up                           | which check stops the loop
#     1 → 2 → None        | From node 1 to None                          | fast is not None is False
#     1 → 2 → 3 → None    | From node 1 to node 3 (its next is None)     | fast.next is not None is False
#
# - Check AFTER moving, not before, because at start, both start on the head, so checking first would say True straight away.
# - Use "slow is fast", not ==, because "is" means the exact same node (the same box),
#   while == means "equal", which a class can define by value (two different nodes holding 5).