# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # finding the length of the list
        fast, slow = head, head

        # wow, so it evaluates fast before fast.next... i did not know
        # find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the latter half of the list
        prev, curr, reverse_head, slow.next = None, slow.next, None, None

        while curr:
            reverse_head = curr.next
            curr.next = prev
            prev = curr
            curr = reverse_head

        list1, list2 = head, prev

        while list2:
            tmp_next1 = list1.next
            tmp_next2 = list2.next
            list1.next = list2
            list2.next = tmp_next1
            list1 = tmp_next1
            list2 = tmp_next2
