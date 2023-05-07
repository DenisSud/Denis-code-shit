def nearest_peak(distance, visited):
    r = -1
    for i in range(len(distance)):
        if r == -1 and not visited[i]:
            r = i
        elif not visited[i] and distance[i] < distance[r]:
            r = i
    return r


def dejkstra(graph, s, f):
    visited = [False] * n
    distance = [float('inf')] * n
    history = [-1] * n
    
    distance[s] = 0

    p = nearest_peak(distance, visited)
    while p != -1:
        row = graph[p]
        for i in range(len(row)):
            if row[i] > 0:
                if distance[p] + row[i] < distance[i]:
                    distance[i] = distance[p] + row[i]
                    history[i] = p
        visited[p] = True
        p = nearest_peak(distance, visited)

    return distance[f], history


n, s, f = map(int, input().split())
s -= 1
f -= 1

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

result, hist = dejkstra(graph, s, f)
if result == float('inf'):
    print(-1)
else:
    # print(result)
    arr = [f]
    while arr[-1] != s:
        ist = hist[arr[-1]]
        arr.append(ist)
    arr.reverse()
    for elem in arr:
        print(elem + 1, end=' ')