curvy = 0
normal = 0
sqare = 0
list = input()
for i in range(len(list)):
    if list[i] == "(":
        normal+=1
    elif list[i] == ")":
        normal-=1
    elif list[i] == "[":
        sqare+=1
    elif list[i] == "]":
        sqare-=1
    elif list[i] == "{":
        curvy+=1
    elif list[i] == "}":
        curvy-=1
if normal == 0 and curvy == 0 and sqare == 0:
    print("yes")
else:
    print("no")