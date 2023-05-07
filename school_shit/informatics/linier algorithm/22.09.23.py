n, k, m = (int(i) for i in (list(map(int, input().split()))))
arr = (list(map(int, input().split())))

y = 1
while (y < n):
    arr[y] += arr[y-1]
    if y >= k+1:
        if arr[y] - arr[y-(k+1)] == m:
            print((y-k+1) + 1)
            break
        elif y == n-1:
            print(0)
    y += 1