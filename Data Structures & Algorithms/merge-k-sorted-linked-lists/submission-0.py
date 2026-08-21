import heapq

class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        heap = [
            (node.val, index, node)
            for index, node in enumerate(lists)
            if node
        ]
        heapq.heapify(heap)

        dummy = ListNode()
        tail = dummy

        while heap:
            _, index, node = heapq.heappop(heap)

            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, index, node.next),
                )

        return dummy.next