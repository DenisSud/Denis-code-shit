n, m = (int(i) for i in (list(map(int, input().split()))))
arr = []

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

max_val = 0
max_lines = []

for j in range(n):
    is_updated = False
    for i in range(m):
        if max_val == arr[j][i] and not is_updated:
            max_lines.append(j)
            is_updated = True
        if arr[j][i]>max_val:
            max_val = arr[j][i]
            max_lines = [j]
            is_updated = True

print(len(max_lines))
for i in max_lines:
    print(i)