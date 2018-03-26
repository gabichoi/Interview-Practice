class BinTree:
    empty = ()

    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left == self.empty and self.right == self.empty:
            return 'BinTree({})'.format(repr(self.label))
        left = 'BinTree.empty' if self.left == self.empty else repr(self.left)
        right = 'BinTree.empty' if self.right == self.empty else repr(self.right)
        return 'BinTree({}, {}, {})'.format(repr(self.label), left, right)

def binTree(tupleTree):
    """A convenience method for succinctly constructing binary trees.  The
    empty tuple or list stands for BinTree.empty; (V,) or [V] stands
    for BinTree(V); (V, T1, T2) or [V, T1, T2] stands for
    BinTree(V, binTree(T1), binTree(T2)).
    >>> binTree((3,
    ...          (1, (), [2]),
    ...          (6, [5], [7])))
    BinTree(3, BinTree(1, BinTree.empty, BinTree(2)), BinTree(6, BinTree(5), BinTree(7)))
    """
    if len(tupleTree) == 0:
        return BinTree.empty
    elif len(tupleTree) == 1:
        return BinTree(tupleTree[0])
    else:
        return BinTree(tupleTree[0], binTree(tupleTree[1]), binTree(tupleTree[2]))
