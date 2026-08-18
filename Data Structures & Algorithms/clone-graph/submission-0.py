"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        oldgraph = [None for i in range(100)]
        newgraph = [None for i in range(100)]

        # bfs
        visited = set()
        q = [node]
        nq = []

        while q:
            for nn in q:
                if nn in visited or nn is None:
                    continue

                oldgraph[nn.val-1] = nn
                newgraph[nn.val-1] = Node(val=nn.val)
                nq.extend(nn.neighbors)
                visited.add(nn)

            q, nq = nq, []


        # 
        for i in range(len(oldgraph)):
            nn = oldgraph[i]
            if not nn:
                break

            for nnn in nn.neighbors:
                newgraph[i].neighbors.append(newgraph[nnn.val-1])

        return newgraph[node.val-1]

        
