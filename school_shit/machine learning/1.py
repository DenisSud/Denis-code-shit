stack = []
end = False
while end == False:
    x = str(input())
    if x[0:4] == "push":
        stack.append(x[-1])
        print("ok")
    elif x[0:4] == "size":
        print(len(stack))
    elif x[0:5] == "clear":
        stack = []
    elif x[0:4] == "back":
        if x != []:
            print(stack[-1])
        else:
            print('erorr')
    elif x[0:4] == "pop":
        if x != []:    
            print(stack[-1])
            stack.pop
        else:
            print('erorr')
    elif x[0:4] == "exit":
        print("buy")
        end = True