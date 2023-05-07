# Open the input file for reading
with open("input.txt", "r") as file:
  # Read the text from the file
  text = file.read()

# Split the text into a list of words
words = text.split()

# Convert the list of words to a set to remove duplicates
words = set(words)

# Print the number of unique words in the text
print(len(words))
