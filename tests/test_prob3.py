from bongo3 import Node, find_ancestors, lca


def test_find_parents_function():
    n1 = Node(1)
    n2 = Node(2, n1)
    n3 = Node(3, n1)
    n4 = Node(4, n2)
    n5 = Node(5, n2)
    n6 = Node(6, n3)
    n7 = Node(7, n3)
    n8 = Node(8, n4)
    n9 = Node(9, n4)

    assert find_ancestors(n9) == [9,4,2,1]


def test_lca_function():
    n1 = Node(1)
    n2 = Node(2, n1)
    n3 = Node(3, n1)
    n4 = Node(4, n2)
    n5 = Node(5, n2)
    n6 = Node(6, n3)
    n7 = Node(7, n3)
    n8 = Node(8, n4)
    n9 = Node(9, n4)

    assert lca(n6,n7) == 3

    assert lca(n3,n7) == 3