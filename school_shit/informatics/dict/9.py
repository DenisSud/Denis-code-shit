n = int(input())
balances = {}

for i in range(n):
    action, *rest = input().split()
    if action == "DEPOSIT":
        persone, amount = rest
        balances[persone] += amount
        
    elif action == "INCOME":
        percent = int(rest)
        for i in balances:
            if balances[i] > 0:
                balances[i] += balances[i]*percent/100
    elif action == "BALANCE":
        persone = rest
        if persone in balances:
            print(action[persone])
        else:
            print("ERROR")
    elif action == "WITHDRAW":
        name, amount = rest
        balances[name] -= amount
    else: #TRANSFER
        name1, name2, amount = rest
        balances[name1] -= amount
        balances[name2] += amount
        