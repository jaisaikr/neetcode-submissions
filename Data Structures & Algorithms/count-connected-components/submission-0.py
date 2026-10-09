class DSU:
    def __init__(self, n):
        self.parent = [-1]*n
        self.size = [0]*n
        for v in range(n):
            self.make_set(v)
        self.count = n
    
    def make_set(self, v):
        self.parent[v] = v
        self.size[v] = 1

    def find_set(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find_set(self.parent[a])
        return self.parent[a]

    def union_sets(self, a, b):
        root_a, root_b = self.find_set(a), self.find_set(b)
        if root_a == root_b:
            return
        
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a,b in edges:
            dsu.union_sets(a,b)
        
        return dsu.count
        
            
