class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0)
        slow, fast = start, start
        start.next = head

        for i in range(n + 1):
            fast = fast.next

        while fast != None:
            fast = fast.next
            slow = slow.next

        # skip desired node
        slow.next = slow.next.next

        return start.next
