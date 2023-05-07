n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
max = 0
max_i = 0
max_j = 0
for j in range(n):
    sum = 0
    for i in range(m):
        sum+=arr[i][j]
        if arr[j][i]>max:
            max = arr[j][i]
            max_i = i
            max_j = j
        elif arr[j][i] == max:
            max_i+=1
    if max_j = sum and 
print(max)
print(max_j)
print(max_i)