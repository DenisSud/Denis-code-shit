n, m = (int(i) for i in (list(map(int, input().split()))))
arr1 = []
arr2 = []
for i in range(m):
    temp = list(map(int, input().split()))
    arr2.append(temp)

for i in range(n):
    arr1.append([])
    for j in range(n):
        arr1[i].append(0)


for x, y in arr2:
    arr1[x - 1][y - 1] = 1
    arr1[y - 1][x - 1] = 1


for i in range(n):
    string = str()
    for j in  range(n):
        string = string + " " + str(arr1[i][j])
    print(string)