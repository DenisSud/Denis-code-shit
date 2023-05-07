n = int(input())
arr = []
arr1 = range(1, n+1)
for i in range(n-1):
    x = int(input())
    arr.append(x)

t = set(arr1) - set(arr)
print(*t)
