# Read the number of vertices
n = int(input())

# Read the adjacency lists
adj_lists = [list(map(int, input().split())) for _ in range(n)]

# Create a mapping from each vertex to its expanded version
expanded = {i: [i + j * n for j in range(n)] for i in range(1, n + 1)}

# Print the number of expanded vertices
print(n ** 2)

# Print the expanded adjacency lists
for i in range(1, n + 1):
    expanded_adjacents = [expanded[adj][i - 1] for adj in adj_lists[i - 1]]
    print(' '.join(str(x) for x in expanded_adjacents))
