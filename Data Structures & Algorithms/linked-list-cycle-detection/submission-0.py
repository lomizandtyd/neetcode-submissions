# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        sl = head
        fs = head.next

        while sl and fs:

            if sl == fs:
                return True

            fs = fs.next
            if fs:
                fs = fs.next

            sl = sl.next

        return False