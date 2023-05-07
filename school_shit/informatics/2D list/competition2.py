n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
max = 0
max_i = 0
max_j = 0
for j in range(n):
    for i in range(m):
        if arr[j][i]>max:
            max = arr[j][i]
            max_i = i
            max_j = j
print(max)
print(max_j)
print(max_i)