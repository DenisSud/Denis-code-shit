# Читаем количество вершин и ребер
n, m = map(int, input().split())

# Создаем словарь для хранения ребер
graph = {}

# Читаем ребра
for i in range(m):
  u, v = map(int, input().split())

  # Добавляем ребро в словарь
  if u in graph:
    if v in graph[u]:
      # Ребро уже существует, значит граф содержит параллельные ребра
      print("YES")
      exit()
    else:
      graph[u].append(v)
  else:
    graph[u] = [v]

# Если мы дошли до этой точки, значит в графе нет параллельных ребер
print("NO")
