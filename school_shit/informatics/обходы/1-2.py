n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)

for i in range(n):
    print(len(adj[i]), end=' ')
    print(*adj[i])
