Return a new Tree, where each entry is the sum of all entries in the corresponding subtree of t.

class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = list(children)

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children
       
def cumulative_sum(t):

    """
    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    
    """
    # return a new Tree
    # for each child in children
        # if the child is a leaf return child 
        # if the child has another, sum itself and its 
    
    def sum_all(t):
        if t.is_leaf():
            return t.label
        else:
            return t.label + sum([sum_all(child) for child in t.children])
   
    if t.is_leaf():
        return Tree(t.label)
    else:
        return Tree(sum_all(t), [cumulative_sum(child) for child in t.children])
