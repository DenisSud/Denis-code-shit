def dfs(v, visited, adj, component):
    visited[v-1] = True
    component.append(v)
    for u in adj[v-1]:
        if not visited[u-1]:
            dfs(u, visited, adj, component)

n = int(input())
adj = [[] for _ in range(n)]
visited = [False] * n
components = []

for i in range(n):
    adj[i] = [j+1 for j, x in enumerate(map(int, input().split())) if x]

for i in range(1, n+1):
    if not visited[i-1]:
        component = []
        dfs(i, visited, adj, component)
        components.append(component)

print(len(components))
for component in components:
    print(len(component))
    print(*component)
