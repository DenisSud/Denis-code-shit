def calc(i, st):
    if i == '+':
        return st[-1] + st[len(st)-2]
    elif i == '-':
        return st[len(st)-2] - st[-1]
    elif i == '*':
        return st[-1] * st[len(st)-2]
    else:
        return st[len(st)-2] // st[-1]


s = input()
st = []
s = ''.join(s.split())
for i in s:
    if i.isdigit():
        st.append(int(i))
    else:
        k = calc(i, st)
        st.pop()
        st.pop()
        st.append(k)
print(st[0])