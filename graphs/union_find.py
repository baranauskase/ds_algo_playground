class UnionFind(object):
    """
    Class that implements union and find algorithms for disjoint sets. The 
    implementation utilises path compression and union rank optimizations.
    """

    def __init__(self, num_nodes):
        self._rank = [1] * num_nodes
        self._nodes = list(range(num_nodes))
        self._root_count = num_nodes

    def union(self, x, y):
        """
        Joins x and y under the same root node
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self._rank[root_x] < self._rank[root_y]:
                self._nodes[root_y] = root_x
            elif self._rank[root_x] > self._rank[root_y]:
                self._nodes[root_x] = root_y
            else:
                self._nodes[root_y] = root_x
                self._rank[root_x] += 1
            self._root_count -= 1

    def find(self, x):
        """
        Finds the root node of x
        """

        if x != self._nodes[x]:
            self._nodes[x] = self.find(self._nodes[x])
        return self._nodes[x]

    def connected(self, x, y):
        """
        Determines if x and y have the same root node
        """
        return self.find(x) == self.find(y)