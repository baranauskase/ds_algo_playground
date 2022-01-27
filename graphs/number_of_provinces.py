"""
There are n cities. Some of them are connected, while some are not. If city a
is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other
cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

"""
from typing import List
from graphs.union_find import UnionFind
class Solution:
    def finde_circle_num(self, is_connected: List[List[int]]) -> int:
        uf = UnionFind(max(len(is_connected), len(is_connected[0])))

        for x in range(len(is_connected)):
            for y in range(len(is_connected[x])):
                if is_connected[x][y] == 1:
                    uf.union(x, y)

        return len([x for idx, x in enumerate(uf._nodes) if x == idx])