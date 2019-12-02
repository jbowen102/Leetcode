"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return "%d" % self.val + "->" + self.next.__repr__()
        else:
            return "%d" % self.val

class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):
        # No guarantee they are the same length.
        # Is it important that the input lists are already sorted?


        if not l1 and not l2:
            # base case
            return None

        if l1 and not l2:
            # quasi-base case
            return l1

        if l2 and not l1:
            # quasi-base case
            return l2

        else:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2


# fails on [5], [1, 2, 4] input.

# test
# node1 = ListNode(1)
# node2 = ListNode(2)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node1.next = node2
# node2.next = node4

# mynode1 = ListNode(1)
# mynode3 = ListNode(3)
# mynode5 = ListNode(5)
# mynode1.next = mynode3
# mynode3.next = mynode5
#
# node2 = ListNode(2)
# node4 = ListNode(4)
# node6 = ListNode(6)
# node2.next = node4
# node4.next = node6

#
# mynode1 = ListNode(1)
# mynode3 = ListNode(3)
# mynode5 = ListNode(5)
# mynode1.next = mynode3
# mynode3.next = mynode5
#
# node2 = ListNode(2)
# node4 = ListNode(4)
# node6 = ListNode(6)
# node8 = ListNode(8)
# node2.next = node4
# node4.next = node6
# node6.next = node8

# mynode1 = ListNode(1)
# mynode3 = ListNode(3)
# mynode5 = ListNode(5)
# mynode7 = ListNode(7)
# mynode1.next = mynode3
# mynode3.next = mynode5
# mynode5.next = mynode7
#
# node2 = ListNode(2)
# node4 = ListNode(4)
# node6 = ListNode(6)
# node8 = ListNode(8)
# node2.next = node4
# node4.next = node6
# node6.next = node8
