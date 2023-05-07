n = int(input())
arr = []
sides = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if (i+1,j+1) not in sides and (j+1,i+1) not in sides:
                sides.append((i+1,j+1))

for x in range(len(sides)):
    string = ""
    for y in range(2):
        if string != str():
            string = string + " " + str(sides[x][y])
        else:
            string = str(sides[x][y])
    print(string)

