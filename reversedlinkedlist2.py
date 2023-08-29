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
        new_next = None

        if cur_node == None:
            return None

        while cur_node != None:
            prev = cur_node
            cur_node = cur_node.next
            prev.next = new_next
            new_next = prev

        return prev