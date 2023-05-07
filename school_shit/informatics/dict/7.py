n = int(input())
files = {}

for i in range(n):
    file, *allowed_actions = input().split()
    if file not in files:
        files[file] = set(allowed_actions)
    else:
        files[file] += (set(allowed_actions))
print(files)   
m = int(input())

for i in range(m):
    request, file = input().split()
    if request == "read":
        request = "R"
    elif request == "write":
        request = "W"
    else:
        request = "x"
    if request in files[file]:
        print("OK")
    else:
        print("Access denied")
