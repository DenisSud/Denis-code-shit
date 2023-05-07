n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    
arr2 = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr2.append([i+1, j+1])

for i in range(len(arr2)):
    string = str()
    for j in  range(2):
        if string != str():
            string = string + " " + str(arr2[i][j])
        else:
            string = str(arr2[i][j])
    print(string)