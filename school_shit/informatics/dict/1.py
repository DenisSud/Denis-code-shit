# dict = {}
# keys = dict.keys()
# val = dict.values()
# pairs = dict.items()

input_file = open('input.txt', 'r')
lines = input_file.readlines()
pure_lines = []
for i in range(len(lines)):
    pure_lines+=lines[i].split()
    
d = {}
for i in range(len(pure_lines)):
    word = pure_lines[i]
    if word not in d:
        d[word] = 0
        
    print(d[word], end=" ")
    d[word]+=1