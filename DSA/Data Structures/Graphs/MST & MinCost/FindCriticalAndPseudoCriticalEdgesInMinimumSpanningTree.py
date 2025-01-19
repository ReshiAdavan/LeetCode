from typing import List

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda x: x[2])

        originalWeight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                originalWeight += w

        critical, pseudo = [], []
        for v1, v2, w, i in edges:
            weight = 0
            uf = UnionFind(n)
            for n1, n2, d, j in edges:
                if i != j and uf.union(n1, n2):
                    weight += d

            if originalWeight < weight or max(uf.rank) != n:
                critical.append(i)
                continue

            uf = UnionFind(n)
            uf.union(v1, v2)

            weight = w
            for n1, n2, d, j in edges:
                if uf.union(n1, n2):
                    weight += d
            if weight == originalWeight:
                pseudo.append(i)

        return [critical, pseudo]

# TC: O(Elog(E) + E * E)
# SC: O(V + E)
