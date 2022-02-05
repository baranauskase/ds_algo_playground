
"""
You have a graph of n nodes. You are given an integer n and an array edges
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in
the graph.

Return the number of connected components in the graph.
"""
from typing import List
from graphs.union_find import UnionFind

class Solution:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for e in edges:
            uf.union(e[0], e[1])

        return uf.root_count
