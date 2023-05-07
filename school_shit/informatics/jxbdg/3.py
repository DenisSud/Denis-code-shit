n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
summ = 0
for i in range(n):
    for j in range(n):
        if i == n-1 or i == 0 or j == n-1 or j == 0:
            summ+=arr[i][j]
print(summ)