class Stack:

  def __init__(self,size):
    self.size = size
    self.__stack = [None] * self.size
    self.top = -1

  def push(self,value):

    if self.top == self.size - 1:
      return "Overflow"
    else:
      self.top+=1
      self.stack[self.top] = value

  def pop(self):

    if self.top == -1:
      return "Empty"
    else:
      data = self.stack[self.top]
      self.top-=1
      print(data)

  def traverse(self):

    for i in range(self.top + 1):
      print(self.stack[i],end=' ')




class Node:

  def __init__(self,value):
    self.data = value
    self.next = None
     

class Stack:

  def __init__(self):
    self.top = None

  def push(self, value):

    new_node = Node(value)

    new_node.next = self.top

    self.top = new_node

  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def is_empty(self):
    return self.top == None

  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data

  def traverse(self):

    temp = self.top

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next

  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      temp = temp.next
      counter+=1

    return counter



def reverse_string(string):
  s = Stack()
  for i in string:

    s.push(i)

  res = ""

  while (not s.is_empty()):
    res = res + s.pop()

  print(res)

     

reverse_string("Haldia")

def text_editor(text,pattern):

  u = Stack()
  r = Stack()

  for i in text:
    u.push(i)

  for i in pattern:

    if i == 'u':
      data = u.pop()
      r.push(data)
    else:
      data = r.pop()
      u.push(data)

  res = ""

  while(not u.is_empty()):
    res = u.pop() + res

  print(res)
     

text_editor("Hello","uurruuuur")
     

def brackets(expr):

  s = Stack()

  for i in expr:

    if i == '(':
      s.push(i)
    elif i == ')':
      if s.peek() == '(':
        s.pop()
      else:
        print("Imbalanced")
        return 

  if (s.is_empty()):
    print("Balanced")
  else:
    print("Imbalanced")


     

L = [
     [0,1,0,0],
     [0,0,1,1],
     [1,0,0,1],
     [0,0,0,0]
]
     

def celebrity(L):

  s = Stack()

  for i in range(len(L)):
    s.push(i)

  while s.size() >= 2:

    i = s.pop()
    j = s.pop()

    if L[i][j] == 0:
      # j is not a celebrity
      s.push(i)
    else:
      # i is not a celebrity
      s.push(j)

  cel = s.pop()

  for i in range(len(L)):

    if i != cel:

      if L[i][cel] != 1 or L[cel][i] != 0:
        print("No celebrity")
        return
  print("Celebrity is",cel)

     

celebrity(L)

s=Stack()
s.push(1)
s.push(2)
s.push(3)

s.size()
     

a = Stack()
b = Stack()
     

def enqueue_stack(value):
  a.push(value)

def dequeue_stack():

  if not b.is_empty():
    b.pop()
  else:
    if a.is_empty():
      print("Empty queue")
    else:
      while(not a.is_empty()):
        data = a.pop()
        b.push(data)

      b.pop()