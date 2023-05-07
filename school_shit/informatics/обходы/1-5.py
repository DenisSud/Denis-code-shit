n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)

for i in range(n):
    for j in adj[i]:
        for k in adj[j-1]:
            if k != i+1 and k not in adj[i]:
                print("NO")
                exit()

print("YES")