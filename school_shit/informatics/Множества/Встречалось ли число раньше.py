nums = [int(s) for s in input().split()]
x = []
for num in nums:
    if num in x:
        print('YES')
    else:
        print('NO')
        x.append(num)
