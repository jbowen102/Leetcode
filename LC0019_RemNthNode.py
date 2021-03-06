"""

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?

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
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    # First program just removes second to last node.
    def removeNthFromEnd(self, head, n):
        if not head.next:
            return head
        elif not head.next.next:
            return head.next
        elif not head.next.next.next:
            head.next = head.next.next
            return head
        else:
            head.next = self.removeNthFromEnd(head.next, n)
            return head


# tests

node2 = ListNode(2)
node4 = ListNode(4)
node6 = ListNode(6)
node8 = ListNode(8)
node2.next = node4
node4.next = node6
node6.next = node8

print(node2)

mysol = Solution()
new_list = mysol.removeNthFromEnd(node2, 2)

print(new_list)
