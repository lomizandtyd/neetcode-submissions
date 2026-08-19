class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}

        if beginWord == endWord or endWord not in wordList:
            return 0

        def form(w):
            for i in range(len(w)):
                w2 = w[:i] + "." + w[i+1:]
                yield w2

        for w in wordList:
            for w2 in form(w):
                if w2 not in graph:
                    graph[w2] = set()
                graph[w2].add(w)


        def bfs(graph, src_word, tgt_word):
            q = []
            nq = []
            visited = set()

            for w in form(src_word):
                q.append(w)

            i = 0

            while q:
                i += 1
                for w in q:
                    if w in visited or w not in graph:
                        continue

                    visited.add(w)
                    if tgt_word in graph[w]:
                        return i + 1

                    for ww in graph[w]:
                        for ww2 in form(ww):
                            if ww2 not in visited:
                                nq.append(ww2)

                q, nq = nq, []

            return 0

        return bfs(graph, beginWord, endWord)
                        




