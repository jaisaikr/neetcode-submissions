class Solution:

    def is_valid(self, first, second):
        cnt = 0
        if len(first) != len(second):
            return False
        
        for i in range(len(first)):
            if first[i] != second[i]:
                cnt +=1
                if cnt > 1:
                    return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # endWord exists in the wordList
        # construct graph using edge list
        
        items = [beginWord, *wordList]
        g = [[] for _ in range(len(items)) ]


        for i in range(len(items)):
            for j in range(i+1, len(items)):
                if self.is_valid(items[i], items[j]):
                    g[i].append(j)
                    g[j].append(i)
        
        # print(g)
        
        # start bfs from beginWord
        dist = [-1]*len(items)
        q = [0]
        dist[0] = 0
        for v in q:
            for u in g[v]:
                if dist[u] == -1:
                    dist[u] = dist[v]+1
                    q.append(u)

        end_item_index = items.index(endWord)
        if dist[end_item_index] == -1:
            return 0
        
        return dist[end_item_index]+1
        
                



        
        