n = int(input())

g = list(map(int, input().split()))

m = int(input())

roads = []
for i in range(m):
    roads.append(list(map(int, input().split())))

min_cost = 0
visited = [False] * n

current_city = 0
visited[current_city] = True

for i in range(1, n):
    lowest_cost = float("inf")
    previous_city = -1
for neighbor in roads[current_city]:
    if not visited[neighbor] and g[neighbor] < lowest_cost:
        lowest_cost = g[neighbor]
    previous_city = neighbor

if lowest_cost < min_cost:
    min_cost = lowest_cost
    current_city = previous_city

visited[current_city] = True

if visited[n - 1]:
    print(min_cost)
else:
    print(-1)
