"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m1 = {}
        m2 = {}

        p1 = head
        n = 0
        l1 = Node(-1)
        w1 = l1
        while p1:
            m1[p1] = n

            p2 = Node(p1.val)
            w1.next = p2
            w1 = p2
            m2[n] = p2

            n += 1
            p1 = p1.next

        p1 = head
        p2 = l1.next

        while p1:
            p2.random = m2[m1[p1.random]] if p1.random else None
            p1 = p1.next
            p2 = p2.next

        return l1.next

