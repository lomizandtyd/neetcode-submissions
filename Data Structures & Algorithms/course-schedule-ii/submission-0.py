class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        indegree = [0] * numCourses

        # pass
        for out_, in_ in prerequisites:
            if in_ not in graph:
                graph[in_] = set()
            
            if out_ not in graph:
                graph[out_] = set()

            graph[in_].add(out_)
            indegree[out_] += 1

        q = []

        # 
        for n in graph.keys():
            if indegree[n] == 0:
                q.append(n)

        # 
        nq = []
        order = []
        for n in range(numCourses):
            if indegree[n] == 0:
                order.append(n)
        while q:
            for n in q:
                for nn in graph[n]:
                    indegree[nn] -= 1
                    if indegree[nn] == 0:
                        nq.append(nn)
                        order.append(nn)
            q, nq = nq, []
        
        #
        for n in graph.keys():
            if indegree[n] > 0:
                return []

        return order