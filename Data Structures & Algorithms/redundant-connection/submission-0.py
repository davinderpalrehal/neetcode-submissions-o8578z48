class UnionFind:

    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        uf = UnionFind(N)

        for x, y in edges:
            if not uf.union(x, y):
                return [x, y]