# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Time complexity: O(n log n) because of sorted()
# Space complexity: O(n) because of the two value lists and the new nodes
# LeetCode runtime: 1 ms


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# First attempt
# Time complexity: O(n log n)
# Space complexity: O(n)

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


# -------------------------------------------------------------------------------------------------



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
    print(to_python_list(sol.mergeTwoLists(build_linked_list([]), build_linked_list([0]))))                # [0]  (one empty)


# What I learned:
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