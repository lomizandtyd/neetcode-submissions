# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return


        l1 = ListNode()
        l2 = ListNode()

        p1 = head
        p2 = head.next

        w1 = l1
        w2 = l2

        while p2:
            p1 = p1.next
            p2 = p2.next.next if p2.next else None

        l2.next = p1.next
        p1.next = None

        p1 = l2.next
        l2.next = None
        while p1:
            p2 = p1.next
            p1.next = l2.next
            l2.next = p1
            p1 = p2

        # interleave
        l1 = head
        w1 = l1

        p1 = l1.next
        p2 = l2.next

        while p1 and p2:
            w1.next = p2
            p3 = p2.next
            p2.next = p1
            w1 = p1
            p1 = p1.next
            p2 = p3


        