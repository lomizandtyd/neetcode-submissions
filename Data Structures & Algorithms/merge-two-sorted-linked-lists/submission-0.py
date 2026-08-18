# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        write = dummy

        cur1 = list1
        cur2 = list2

        while cur1 and cur2:
            if cur1.val <= cur2.val:
                write.next = cur1
                cur1 = cur1.next
            else:
                write.next = cur2
                cur2 = cur2.next

            write = write.next

        if not cur1:
            cur1 = cur2

        if cur1:
            write.next = cur1

        return dummy.next