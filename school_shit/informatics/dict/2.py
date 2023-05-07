#input
n = int(input())

dict = {}
for i in range(n):
    words = input().split()
    dict[words[0]] = words[1]
    dict[words[1]] = words[0]

#logic
sinonim = input()
print(dict[sinonim])