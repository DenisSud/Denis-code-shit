# отрезок с максимальной суммой 
def max_subarray(numbers):
    best_sum = 0
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

# элементы с максимальной разностью
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

print(imin, imax)
# запрос суммы отрезка
a = [1, 3, 7, 10, 0]
i = 0
j = 2

y = 1
while (y < len(a)):
    a[y] += a[y-1]
    y += 1
a[j] - a[i]
# отрезок заданной суммы

n, k, m = (int(i) for i in (list(map(int, input().split()))))
arr = (list(map(int, input().split())))

y = 1
while (y < n):
    y += 1
    arr[y] += arr[y-1]
    if y >= k:
        if arr[y] - arr[y-(k+1)] == m:
            print(y-k)
            break
        else:
            print(0)
    