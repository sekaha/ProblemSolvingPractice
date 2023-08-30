# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2!=None:
            new_head = list2
        elif list2 == None and list1!=None:
            new_head = list1
        else:
            new_head = None

        while (list1 != None) and (list2 != None):
            if list1.val <= list2.val:
                if new_head == None:
                    new_head = list1
                
                temp_next1 = list1.next
                list1.next = list2
                temp_next2 = list2.next
                list2.next = temp_next1
                list2 = temp_next2
                list1 = temp_next1
            else:
                if list1.next != None:
                    list1 = list1.next
                else:
                    if new_head == None:
                        new_head = list2

                    temp_next1 = list2.next
                    list2.next = list1
                    temp_next2 = list1.next
                    list1.next = temp_next1
                    list1 = temp_next2
                    list2 = temp_next1
        
        return new_head