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


    # refactor to test if vals are present instead of next


        if l1.next and l2.next:
            n1 = ListNode(l1.val)
            n2 = ListNode(l2.val)

            n1.next = n2
            n2.next = self.mergeTwoLists(l1.next, l2.next)
            return n1

        if l1.next and not l2.next:
            # quasi-base case
            l2.next = l1.next
            l1.next = l2
            return l1

        if l2.next and not l1.next:
            # quasi-base case
            l1.next = l2
            return l1

        else:
            # base case
            l1.next = l2
            return l1



# fails on [], [] input.



# test
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
# # node8 = ListNode(8)
# node2.next = node4
# node4.next = node6
# # node6.next = node8
