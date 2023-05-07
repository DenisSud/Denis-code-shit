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
    
    distance[s] = 0

    p = nearest_peak(distance, visited)
    while p != -1:
        row = graph[p]
        for i in range(len(row)):
            if row[i] != 0:
                if distance[p] + row[i] < distance[i]:
                    distance[i] = distance[p] + row[i]
        visited[p] = True
        p = nearest_peak(distance, visited)

    return distance[f]


n = int(input())
loop = False
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
for i in range(n):
    if dejkstra(graph, i, i) == 0:
        loop = True
        print(dejkstra(graph, i, i))
        
if loop:
    print(1)
else:
    print(0)