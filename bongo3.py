from utils import first_common_occurrence, measureTime


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


def find_ancestors(nd):
    ancestors_list = [nd.value] # since a node itself is its ancestor
    while nd.parent:
        ancestors_list.append(nd.parent.value)
        nd = nd.parent

    return ancestors_list


@measureTime # decorator to measure the execution time
def lca(nd1, nd2):
    node1_ancestors = find_ancestors(nd1)
    node2_ancestors = find_ancestors(nd2)
    lca_of_two = first_common_occurrence(node1_ancestors, node2_ancestors)

    print(f"LCA for two nodes {nd1.value} and {nd2.value} is {lca_of_two}")
    return lca_of_two


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2, n1)
    n3 = Node(3, n1)
    n4 = Node(4, n2)
    n5 = Node(5, n2)
    n6 = Node(6, n3)
    n7 = Node(7, n3)
    n8 = Node(8, n4)
    n9 = Node(9, n4)

    lca(n9, n7)



