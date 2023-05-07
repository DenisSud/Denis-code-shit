k = int(input())
arr = []
for i in range(k):
    temp = list(map(int, input().split()))
    arr.append(temp)
for i in range(k):
    arr[i].remove(arr[i][0])
    for j in arr[i]:
        arr[0].append(arr[i][j])
        arr[i].pop()
        print(i, 0)
for z in range(k):
    if arr[arr[z][-1]][-1] == arr[z][-1]:
        arr[arr[z][-1]].append(arr[z][-1])
        arr[z].pop()
        print(z, arr[z][-1])
    else:
        z = arr[z][-1]
        if arr[arr[z][-1]][-1] == arr[z][-1]:
            arr[arr[z][-1]].append(arr[z][-1])
            arr[z].pop()
            print(z, arr[z][-1])
            
print(arr)