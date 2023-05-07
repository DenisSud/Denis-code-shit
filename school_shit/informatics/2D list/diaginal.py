n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []
count = 0
tr = True
for i in range(n):
    arr.append([])
for j in range(m):
    arr[i].append(0)
    if j == 0 and i == 1:
        arr[i][j] = 1
    arr[i][j] = count
    count += 1
    while tr:
        