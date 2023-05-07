n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []
for i in range(n):
    arr.append([0]*n)
    
side = []
for i in range(m):
    x, y = (int(i) for i in (list(map(int, input().split()))))
    arr[x-1][y-1] = 1

for i in range(n):
    string = str()
    for j in  range(n):
        x = 3-len(str(arr[i][j]))
        string = string + " "*x + str(arr[i][j])
    print(string)