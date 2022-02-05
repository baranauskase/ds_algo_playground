
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

        swap_done = True
        out = list(s)
        while swap_done:
            swap_done = False
            for i in range(len(s)):
                root = uf.find(i)
                if i < root and out[root] < out[i]:
                    out[i], out[root] = out[root], out[i]
                    swap_done = True
                elif root < i and out[i] < out[root]:
                    out[i], out[root] = out[root], out[i]
                    swap_done = True

        return ''.join(out)