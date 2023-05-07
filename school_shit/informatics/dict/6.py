#parse input
n = int(input())
dictionary = {}
for i in range(n):
    word = input()
    stress_index = word.index(word.upper()[0])
    if word[:stress_index] + word[stress_index+1:] in dictionary:
        dictionary[word[:stress_index] + word[stress_index+1:]].append(stress_index)
    else:
        dictionary[word[:stress_index] + word[stress_index+1:]] = [stress_index]

text = input()
text = text.split(" ")
mistakes = 0
for word in text:
    if word.upper()[0] not in word:
        mistakes += 1
    elif word.upper()[0] in word and word[:word.index(word.upper()[0])] + word[word.index(word.upper()[0])+1:] not in dictionary:
        mistakes += 1
    elif word.upper()[0] in word and word.index(word.upper()[0]) not in dictionary[word[:word.index(word.upper()[0])] + word[word.index(word.upper()[0])+1:]]:
        mistakes += 1
        
print(mistakes)
