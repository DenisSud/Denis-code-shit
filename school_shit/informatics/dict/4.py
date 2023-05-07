import string

text = input()
text = text.lower()
text = text.translate(text.maketrans("", "", string.punctuation))

word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

for word in sorted_words:
    print(word[0])
