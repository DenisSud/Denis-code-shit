n = int(input())
arr = []
sides = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if [i,j] not in sides:
                sides.append([i,j])

print(len(sides))
