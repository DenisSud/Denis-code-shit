def count_descendants(tree):
    # create a dictionary to store the number of descendants for each tree element
    descendants = {}

    # create a dictionary to store the children of each tree element
    children = {}

    # initialize the number of descendants for each element to 0
    for element in tree:
        descendants[element] = 0

    # populate the children dictionary
    for element in tree:
        parent = tree[element]
        if str(parent) not in children:
            children[str(parent)] = []
        children[str(parent)].append(element)

    # traverse the tree in postorder and update the number of descendants for each element
    stack = ['Peter_I'] # start with the root node
    while stack:
        element = stack.pop()
        for child in children.get(element, []):
            stack.append(child)
            descendants[element] += descendants[child] + 1

    # sort the elements lexicographically and print the number of descendants for each
    for element in sorted(tree.keys()):
        print(f"{element} {descendants[element]}")

def build_family_tree(n, relationships):
    # create an empty dictionary to store the family tree
    tree = {}

    # iterate over the relationships and add each element to the tree
    for i in range(n-1):
        child, parent = relationships[i].split()
        if parent not in tree:
            tree[parent] = []
        tree[parent].append(child)

    # return the family tree dictionary
    return tree
n = int(input())
rel = []
for i in range(n-1):
    rel.append(input())
count_descendants(build_family_tree(n, rel))