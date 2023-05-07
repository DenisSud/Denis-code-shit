n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []
count = 0
back = False
for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i].append(count)
        count += 1
    if back == True:
        back = False
        arr[i].reverse()
    else:
        back = True
        
for i in range(n):
    string = str()
    for j in  range(m):
        x = 3-len(str(arr[i][j]))
        string = string + " "*x + str(arr[i][j])
    print(string)