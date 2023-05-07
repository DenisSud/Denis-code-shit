def dfs(v, visited, adj, tree):
    visited[v-1] = True
    for u in adj[v-1]:
        if not visited[u-1]:
            tree.append((v, u))
            dfs(u, visited, adj, tree)

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
visited = [False] * n
tree = []

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)

dfs(1, visited, adj, tree)

for edge in tree:
    print(*edge)
