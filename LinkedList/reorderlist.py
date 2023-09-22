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
        front = head

        # move the front node pointer towards the back (middle by end) until there are no more children
        for i in range(2):
            print(front.val)
            # init them to the same position
            back = front

            # zoom the back pointer the n-1 node
            while back.next.next != None:
                back = back.next

            print(back.val)

            # To traverse the nodes in original order, we need a temp next node
            tmp_next = front.next

            print(tmp_next.val)

            # insert back node between front and front.next
            # backnode's prev needs its next set to None
            front.next, back.next.next, back.next = back.next, front.next, None

            front = tmp_next
