n = int(input())
adj = [[] for _ in range(n)]

for i in range(n):
    adj[i] = list(map(int, input().split()))[1:]

for i in range(n):
    for j in adj[i]:
        print(len(adj[j-1]), end=' ')
        print(*adj[j-1])
