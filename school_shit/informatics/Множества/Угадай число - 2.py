# Read the input
n = int(input())

# Initialize a set to keep track of the possible numbers August could be thinking of
possible_numbers = set(range(1, n+1))

# Read the questions and answers
while True:
  # Read a line of input
  line = input()

  # If it is the last line, break out of the loop
  if line == "HELP":
    break

  # Split the line into a list of numbers
  numbers = set(map(int, line.split()))

  # If the set of numbers contains exactly half of the possible numbers,
  # print "NO" and remove all numbers from the set of possible numbers
  if len(numbers) == len(possible_numbers) / 2:
    print("NO")
    possible_numbers.clear()
  # Otherwise, print "YES" and update the set of possible numbers
  # to the intersection of the current set and the set of numbers
  else:
    print("YES")
    possible_numbers.intersection_update(numbers)

# Print the remaining possible numbers, sorted in ascending order
print(" ".join(str(x) for x in sorted(possible_numbers)))
