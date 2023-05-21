m = []
while True:
    inp = int(input())
    if inp == 0:
        break
    m.append(inp)
summ = 0
n = 0
for i in range(len(m)):
    if not m[i] % 8:
        summ += m[i]
        n += 1
if n > 0:
    print(round(summ/n, 1))
else:
    print("NO")