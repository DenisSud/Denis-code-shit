# Читаем количество вершин
n = int(input())

# Создаем список для хранения степеней вершин
degrees = [0] * n

# Читаем матрицу смежности
matrix = []
for i in range(n):
  matrix.append(list(map(int, input().split())))

# Находим степени вершин
for i in range(n):
  for j in range(n):
    if matrix[i][j] == 1:
      degrees[i] += 1

# Выводим степени вершин
for i in degrees:
    print(i)
# print(" ".join(map(str, degrees)))
