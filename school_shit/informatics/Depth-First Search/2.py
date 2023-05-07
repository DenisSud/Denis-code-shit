n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []
for i in range(n):
    arr.append([])
    
sides = []
for i in range(m):
    sides.append(input().split)
    
for i in sides:
    arr[i[0]].append(i[1])
    
for i in arr:
    string = str()
    string = string + str(len(i))
    for j in i:
        string = string + str(j)
    print(string)