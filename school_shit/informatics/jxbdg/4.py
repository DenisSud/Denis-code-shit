a = [9000, 2, 8, 9, 1]
imax = len(a) - 1
imin = 0
imin_new = 0

for i in range(len(a)):
    if (a[imax] - a[imin] < a[i] - a[imin_new]):
        imax = i
        imin = imin_new
    elif (a[imin_new] > a[i]):
        imin_new = i
print(imin)