class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.top = None

class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    newnode.data = data;
    newnode.next = top;
    top = newnode;

  def pop(self) -> None:
    # Write your code here
    if(top==None):
      print("Unerflow")
    else:
      struct Node* temp = top;
      top = top.next;
      free (temp);

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  

# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
