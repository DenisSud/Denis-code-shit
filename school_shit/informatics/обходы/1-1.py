tree = dict()
n = int(input())
for i in range(n-1):
    potomok, predok = input().split()
    tree[potomok] = predok
    if predok not in tree:
        tree[predok] = ""

level_tree = dict()
for item in tree:
    potomok = item
    count = 0
    while tree[potomok]!="":
        count += 1
        potomok = tree[potomok]
        
    
    level_tree[item] = count
    
for i in sorted(level_tree):
    out = i + " " + str(level_tree[i])
    print(out)