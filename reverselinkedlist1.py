# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(node):
            if node.next != None:
                new_head = helper(node.next)
                node.next.next = node
                return new_head
            else:
                return node
        
        if head == None:
            return None
        
        new_head = helper(head)
        head.next = None

        return new_head