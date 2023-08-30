# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# I somewhat overcomplicated this :((
class Solution(object):
    def reverseList(self, head):
        cur_node = head
        prev = None

        while cur_node != None:
            new = cur_node
            cur_node = cur_node.next
            new.next = prev
            prev = cur_node

        return prev