# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l1 = ListNode()
        l1.next = head

        p1 = l1
        p2 = l1

        for i in range(n):
            p2 = p2.next
            if not p2:
                break

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next if p1.next else None

        return l1.next