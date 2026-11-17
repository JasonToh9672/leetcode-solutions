# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Time complexity: O(n + m)   (n, m = the lengths of the two lists)
# Space complexity: O(1)
# LeetCode runtime: 1 ms


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# First attempt
# Time complexity: O(n log n)
# Space complexity: O(n)
"""
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = None
        list1_value = []
        list2_value = []
        current1 = list1    # list1 and list2 are the HEAD nodes of linked lists, not Python lists
        current2 = list2
        while current1 is not None:
            list1_value.append(current1.val)    # job 1: use the node I'm on
            current1 = current1.next            # job 2: move to the next node
        while current2 is not None:
            list2_value.append(current2.val)
            current2 = current2.next
        new_list = sorted(list1_value + list2_value)
        for value in reversed(new_list):        # build backwards: each new node goes in front
            head = ListNode(value, head)
        return head
"""


# -------------------------------------------------------------------------------------------------
# Second attempt
# Time complexity: O(n + m)
# Space complexity: O(1)

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()  # a fake first node, so tail always points at a real node, never None
        tail = dummy        # tail = the last node of the result, so I can attach with tail.next = node
        while list1 is not None and list2 is not None:  # "and": I compare both fronts, so if one list is None there's nothing to compare
            if list1.val <= list2.val:  # take the smaller front (if equal, take list1's)
                tail.next = list1       # attach list1's front node after tail
                list1 = list1.next      # move list1's finger to its next node
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next            # move tail onto the node just attached
        if list1 is not None:
            tail.next = list1           # attach the WHOLE rest of list1 (its nodes are already linked together)
        elif list2 is not None:
            tail.next = list2
        return dummy.next               # skip the fake node: the real result starts after it


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
    print(to_python_list(sol.mergeTwoLists(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4]))))   # [1, 1, 2, 3, 4, 4]
    print(to_python_list(sol.mergeTwoLists(build_linked_list([]), build_linked_list([]))))                 # []   (both empty)
    print(to_python_list(sol.mergeTwoLists(build_linked_list([]), build_linked_list([0]))))                # [0]  (list1 empty)
    print(to_python_list(sol.mergeTwoLists(build_linked_list([5]), build_linked_list([1, 2, 3]))))         # [1, 2, 3, 5]  (leftover from list1)


# What I learned:
# First attempt:
# - On LeetCode, list1 and list2 are NOT Python lists. Each one is a head node (the first box of a linked list),
#   so "list1 + list2" gave a TypeError, because Python doesn't know how to add two ListNode objects.
# - My local test used Python lists, so it didn't show the same error as LeetCode.
#   Fix: build the test input with build_linked_list, so it matches what LeetCode gives.
# - My first loop never stopped, because I forgot to move to the next node (current1 = current1.next).
#   Each round of the walking pattern has 2 jobs: 1) use the node I'm on  2) move to the next node
# - Time is O(n log n), not O(n), because sorting n values costs about n * log n steps.
#     O(log n)   → less work than reading the list once (like binary search)   ~20 steps for 1,000,000
#     O(n)       → look at every item once                                     1,000,000 steps
#     O(n log n) → what sorting costs                                          ~20,000,000 steps
# - Empty list: when the head is None, the while loop never runs (the condition is False from the start),
#   so the value list stays [], nothing is built, and the result is None (an empty linked list).
#
# Second attempt:
# - Both lists are already sorted, so each round I only compare the two front node values
#   and attach the smaller one. No sorting, so time is O(n + m).
# - Space is O(1): the only new node is one dummy. Everything else is re-linking the existing nodes
#   by changing their .next arrows (no new nodes, no Python lists).
# - The dummy is a fake first node, so tail is never None, and round 1 works the same as every round.
#   At the end I return dummy.next to skip the fake node.
# - tail remembers the last node of the result, so I can attach there without walking from the start each time.
# - Adding at the back (with tail) keeps the order I take the nodes in; adding at the front would reverse it.
# - The while loop uses AND, so it stops when ONE list is empty. The other list's leftover nodes are
#   all bigger and already sorted, so I attach the whole rest in one step.
#
#   Round by round (list1 = 1 → 2 → 4, list2 = 1 → 3 → 4):
#     start:    dummy                          (tail on dummy)
#     round 1:  dummy → 1                      (took list1's 1)
#     round 2:  dummy → 1 → 1                  (took list2's 1)
#     round 3:  dummy → 1 → 1 → 2              (took list1's 2)
#     round 4:  dummy → 1 → 1 → 2 → 3          (took list2's 3)
#     round 5:  dummy → 1 → 1 → 2 → 3 → 4      (took list1's 4, list1 is now empty → loop stops)
#     leftover: dummy → 1 → 1 → 2 → 3 → 4 → 4  (attached the rest of list2)
#     return dummy.next → 1 → 1 → 2 → 3 → 4 → 4