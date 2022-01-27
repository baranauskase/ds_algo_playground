from graphs.union_find import UnionFind

def test_union_find():
    uf = UnionFind(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)

    assert uf.connected(1, 5)
    assert uf.connected(5, 7)
    assert not uf.connected(4, 9)

    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    assert uf.connected(4, 9)
