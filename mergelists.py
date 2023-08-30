# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        prev = dummy

        while (list1 != None) and (list2 != None):
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1 == None and list2!=None:
            prev.next = list2
        elif list2 == None and list1!=None:
            prev.next = list1
        
        return dummy.next