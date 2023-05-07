input_file = open('input.txt', 'r')
lines = input_file.readlines()
words = []
for i in range(len(lines)):
    words+=lines[i].split()
    
d = {}
for i in range(len(words)):
    word = words[i]
    if word not in d:
        d[word] = 0
    d[word] += 1
    
max_val = 0
max_word = ""
for k in sorted(d):
    if d[k] > max_val:
        max_val = d[k]
        max_word = k
print(max_word)
    
        
