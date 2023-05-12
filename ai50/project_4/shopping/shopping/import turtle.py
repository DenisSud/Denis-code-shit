# define the stack class
class Stack:
  def __init__(self):
    # initialize the stack as an empty list
    self.items = []

  def push(self, item):
    # push an item onto the stack
    self.items.append(item)
    print("ok")

  def pop(self):
    # pop an item off the stack
    if len(self.items) == 0:
      print("error")
    else:
      print(self.items.pop())

  def back(self):
    # return the last item on the stack without removing it
    if len(self.items) == 0:
      print("error")
    else:
      print(self.items[-1])

  def size(self):
    # return the number of items on the stack
    print(len(self.items))

  def clear(self):
    # clear the stack
    self.items = []
    print("ok")

  def exit(self):
    # exit the program
    print("bye")
    return

# initialize the stack
stack = Stack()

# read the input
while True:
  command = input().split()

  # determine which operation to perform
  if command[0] == "push":
    stack.push(int(command[1]))
  elif command[0] == "pop":
    stack.pop()
  elif command[0] == "back":
    stack.back()
  elif command[0] == "size":
    stack.size()
  elif command[0] == "clear":
    stack.clear()
  elif command[0] == "exit":
    stack.exit()
    break
