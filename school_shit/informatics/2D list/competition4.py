n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

max_val = 0
max_lines = 0

for j in range(n):
    is_updated = False
    for i in range(m):
        if max_val == arr[j][i] and not is_updated:
            max_lines += 1
            is_updated = True
        if arr[j][i]>max_val:
            max_val = arr[j][i]
            max_lines = 1
            is_updated = True

print(max_lines)