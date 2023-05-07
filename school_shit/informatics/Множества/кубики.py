a, b = (int(i) for i in (list(map(int, input().split()))))
cubes_a = set()
cubes_b = set()
ans = set()


for i in range(a):
    cubes_a.add(int(input()))
    
for i in range(b):
    new_cube = int(input())
    if new_cube in cubes_a:
        cubes_a.remove(new_cube)
        ans.add(new_cube)
    else:
        cubes_b.add(new_cube)

ans = list(ans)
ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')
    
cubes_a = list(cubes_a)
cubes_a.sort()
print()
print(len(cubes_a))
for i in cubes_a:
    print(i, end=' ')
    
    
cubes_b = list(cubes_b)
cubes_b.sort()
print()
print(len(cubes_b))
for i in cubes_b:
    print(i, end=' ')