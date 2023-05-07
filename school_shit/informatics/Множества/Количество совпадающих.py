list1 = list(input().split())
list2 = list(input().split())
num = list(set(list1).intersection(list2))
print(len(num))