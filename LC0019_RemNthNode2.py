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
        nodelist = []

        # add all nodes to a list so their position can be indexed.
        current_node = head
        while current_node:
            nodelist.append(current_node)
            current_node = current_node.next


        if len(nodelist) < n:
            # includes empty list
            return head
        elif len(nodelist) == n:
            return head.next
        elif n < 2:
            nodelist[-2].next = None
            return head
        else:
            pos_to_remove = len(nodelist) - n
            node_to_remove = nodelist[pos_to_remove]

            node_to_modify = nodelist[pos_to_remove - 1]
            new_next_node = nodelist[pos_to_remove + 1]

            node_to_modify.next = new_next_node

            return nodelist[0]


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
new_list = mysol.removeNthFromEnd(node2, 5)
# new_list = mysol.removeNthFromEnd(node2, 4)
# new_list = mysol.removeNthFromEnd(node2, 3)
# new_list = mysol.removeNthFromEnd(node2, 2)
# new_list = mysol.removeNthFromEnd(node2, 1)
# new_list = mysol.removeNthFromEnd(node2, 0)

print(new_list)
