def add_child(node, child, nodes):
    if node not in nodes:
        nodes[node] = []
    nodes[node].append(child)

def find_lca(root, a, b, nodes):
    if root is None:
        return None
    if root == a or root == b:
        return root
    lca_candidates = []
    for child in nodes[root]:
        lca = find_lca(child, a, b, nodes)
        if lca is not None:
            lca_candidates.append(lca)
    if len(lca_candidates) == 2:
        return root
    elif len(lca_candidates) == 1:
        return lca_candidates[0]
    else:
        return None

n = int(input())
nodes = {}
root = None
for i in range(n):
    parent, child = input().split()
    add_child(parent, child, nodes)
    if parent == "root":
        root = parent

q = int(input())
for i in range(q):
    a, b = input().split()
    lca = find_lca(root, a, b, nodes)
    print(lca)
