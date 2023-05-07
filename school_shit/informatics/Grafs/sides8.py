n, m = map(int, input().split())

# создаем хеш-таблицу
edges = {}

# вводим ребра и заполняем таблицу
for i in range(m):
    u, v = map(int, input().split())
    if (u, v) in edges:
        edges[(u, v)] += 1
    else:
        edges[(u, v)] = 1

# проверяем, содержит ли граф параллельные ребра
has_parallel_edges = False
for u, v in edges:
    if edges[(u, v)] > 1:
        has_parallel_edges = True
        break

if has_parallel_edges:
    print("YES")
else:
    print("NO")
