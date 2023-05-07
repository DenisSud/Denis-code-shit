n, m = (int(i) for i in (list(map(int, input().split()))))
A = list()
j = []

# for i in range(n):
#     A.append([])
#     for j in range(m):
#         A[i].append(0)
        


x = 0
for i in range(n):
    A.append([])
    A[i][0]=1
    for j in range(m):
        A[i].append(0)
        A[0][j]=1
        if i != 0 or j != 0:
            A[i][j]=A[i-1][j]+A[i][j-1]
            
            
for i in range(n):
    string = ""
    for j in range(m):
        string = string + "     " + str(A[i][j])
    print(string)

# i = 0
# j = 0
# while len(A) != n and len(A[n-1]) != m:\
#     if i == 0 or j == 0:
        