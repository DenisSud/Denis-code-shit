n = int(input())
arr = []
loop = False

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

for i in range(n):
    if arr[i][i] == 1:
        loop = True

if loop == True:
    print("YES")
else:
    print("NO")