"""
https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self.next:
            repr_str = "%d -> " % self.val
            repr_str += self.next.__repr__()
        else:
            repr_str = "%d" % self.val
        return repr_str

class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
        ones = (l1.val+l2.val) % 10
        overflow = (l1.val+l2.val >= 10)

        new_node = ListNode(ones)

        if l1.next and l2.next:
            # add one to the next node's (more significant) digit
            if overflow:
                l1.next.val += 1

            # get the next ListNode in the chain (more significant digit)
            next_node = self.addTwoNumbers(l1.next, l2.next)

            new_node.next = next_node
            return new_node

        if l1.next:
            # get the next ListNode in the chain (more significant digit)
            if overflow:
                next_node = self.addTwoNumbers(l1.next, ListNode(1))
            else:
                next_node = l1.next

            new_node.next = next_node
            return new_node

        if l2.next:
            # get the next ListNode in the chain (more significant digit)

            if overflow:
                next_node = self.addTwoNumbers(ListNode(1), l2.next)
            else:
                next_node = l2.next

            new_node.next = next_node
            return new_node

        elif overflow:
            # If no existing node exists to add to, make one.
            next_node = ListNode(1)
            new_node.next = next_node
            return new_node

        else:
            new_node.next = None
            return new_node

# 80 ms runtime on Leetcode

# Test cases
# 281
node1 = ListNode(1)
node1.next = ListNode(8)
node1.next.next = ListNode(2)

# 615320
node2 = ListNode(0)
node2.next = ListNode(2)
node2.next.next = ListNode(3)
node2.next.next.next = ListNode(5)
node2.next.next.next.next = ListNode(1)
node2.next.next.next.next.next = ListNode(6)

# 11
node3 = ListNode(1)
node3.next = ListNode(1)

# 41
node4 = ListNode(1)
node4.next = ListNode(4)






#
