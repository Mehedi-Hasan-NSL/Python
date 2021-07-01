# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:19:57 2021

@author: DELL
"""

class Node():
    def __init__(self, data):
      self.data = data
      self.next = None

class Stack():
    def __init__(self):
      self.head = None
      self.top = None

def traversal(s):
    temp = s.head #temporary pointer to point to head
    
    a = ''
    while temp != None: #iterating over stack
      a = a+str(temp.data)+'\t'
      temp = temp.next
    
    print(a)

def is_empty(s):
    if s.top == None:
      return True
    return False

def push(s, n):
    if is_empty(s): #empty
      s.head = n
      s.top = n
    else:
      s.top.next = n
      s.top = n

def pop(s):
    if is_empty(s):
      print("Stack Underflow")
      return -1000
    else:
      x = s.top.data
      if s.top == s.head: # only one node
        s.top = None
        s.head = None
      else:
        temp = s.head
        while temp.next != s.top: #iterating to the last element
          temp = temp.next
        temp.next = None
        del s.top
        s.top = temp
        
      print("Poping ",x)
      return x

if __name__ == '__main__':
    s = Stack()
    
    a = Node(10)
    b = Node(20)
    c = Node(30)
    
    pop(s)
    push(s, a)
    push(s, b)
    push(s, c)
    
    traversal(s)
    pop(s)
    traversal(s)