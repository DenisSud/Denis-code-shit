# Читаем размеры массива
n, m = map(int, input().split())

# Создаем массив A
A = [[0] * m for i in range(n)]

# Заполняем массив A
for i in range(n):
  for j in range(m):
    A[i][j] = i * j

# Выводим массив A
for row in A:
  print(" ".join(map(str, row)))
