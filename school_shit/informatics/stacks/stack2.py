def push(a,n):
    a.append(n)
    print('ok')

def pop(a):
    if len(a)>0:
        print(a.pop())
    else:
        print('error')

def back(a):
    if len(a)>0:
        print(a[-1])
    else:
        print('error')
def size(a):
    print(len(a))
def clear(a):
    a=[]
    print('ok')
a=[]
word=input()
while 'exit' not in word:
    if 'size' in word:
        size(a)
    elif 'pop' in word:
        pop(a)
    elif 'back' in word:
        back(a)
    elif 'clear' in word:
        clear(a)
    else:
        push(a,int(list(map(str,word.split()))[-1]))
    word=input()
print('bye')