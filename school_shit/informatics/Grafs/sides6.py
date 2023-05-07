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


for i in range(n):
    for j in range(n):
        if [i+1, j+1] in arr2:
            arr1[i][j] = 1


for i in range(n):
    string = str()
    for j in  range(n):
        if string != str():
            string = string + " " + str(arr1[i][j])
        else:
            string = str(arr1[i][j])
    print(string)