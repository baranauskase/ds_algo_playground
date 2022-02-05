"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n
and a list of edges where edges[i] = [ai, bi] indicates that there is an
undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""
from typing import List
from graphs.union_find import UnionFind


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for edge in edges:
            if uf.connected(edge[0], edge[1]):
                return False
            uf.union(edge[0], edge[1])

        return uf.root_count == 1