class UnionFind:

    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] < self.rank[parent_y]:
                self.parent[parent_x] = parent_y
            elif self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1
            return True
        return False


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        count = n

        for src, dst in edges:
            if uf.union(src, dst):
                count -= 1
        
        return count