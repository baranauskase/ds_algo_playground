
"""
You are given a string s, and an array of pairs of indices in the string pairs
where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number
of times.

Return the lexicographically smallest string that s can be changed to after
using the swaps.
"""

from typing import List
from graphs.union_find import UnionFind

class Solution:
    def smallest_string_with_swaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))

        for p in pairs:
            uf.union(p[0], p[1])

        local_s = {}

        for i in range(len(s)):
            root = uf.find(i)
            if root not in local_s:
                local_s[root] = []

            local_s[root].append(s[i])

        for v in local_s.values():
            v.sort()

        out = [None] * len(s)

        for i in reversed(range(len(s))):
            root = uf.find(i)
            out[i] = local_s[root].pop()

        return ''.join(out)