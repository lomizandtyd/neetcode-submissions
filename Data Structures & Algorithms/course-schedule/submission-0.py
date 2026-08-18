class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = [0] * numCourses

        # pass
        for in_, out_ in prerequisites:
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
        while q:
            for n in q:
                for nn in graph[n]:
                    indegree[nn] -= 1
                    if indegree[nn] == 0:
                        nq.append(nn)
            q, nq = nq, []
        
        #
        for n in graph.keys():
            if indegree[n] > 0:
                return False

        return True