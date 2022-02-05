"""

There are n people in a social group labeled from 0 to n - 1. You are given an
array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be
friends at the time timestamp i.

Friendship is symmetric. That means if a is friends with b, then b is friends
with a. Also, person a is acquainted with a person b if a is friends with b, or
a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every
other person. If there is no such earliest time, return -1.
"""
from typing import List
from graphs.union_find import UnionFind

class Solution:
    def earliest_acq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)

        for l in sorted(logs, key=lambda x: x[0]):
            uf.union(l[1], l[2])

            if uf.root_count == 1:
                return l[0]

        return -1

