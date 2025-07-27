class Union:
    def __init__(self, size):
        self.parent = list(range(2*size))

    def find_root(self, i):
        if self.parent[i] == i:
            return i

        return self.find_root(self.parent[i])

    def add(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)

        self.parent[root_i] = root_j

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        size = 0
        for x, y in stones:
            size = max(size, x, y)

        size += 1
        u = Union(size)
        for x, y in stones:
            u.add(x, size + y)

        distinct_nodes = []
        for x, y in stones:
            distinct_nodes.append(u.find_root(x))
            distinct_nodes.append(u.find_root(size+y))

        return len(stones) - len(set(distinct_nodes))
