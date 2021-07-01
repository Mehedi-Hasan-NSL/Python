# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:09:05 2021

@author: DELL
"""

class Stack:
    def __init__(self, max_size): #initialize a stack of max_size
        self.top_pointer = -1 #Keep track of top element using this
        self.stack = [None for x in range(max_size)]  #create a list of max_size
    
    def push(self, new_element):
        if self.top_pointer < len(self.stack) - 1:
            self.top_pointer = self.top_pointer + 1 #Move the pointer
            self.stack[self.top_pointer] = new_element #Add the new_element to the top
        else :
            print("Overflow")
    def pop(self):    
        if self.top_pointer >= 0 :
            last_element = self.stack[self.top_pointer]
            del self.stack[self.top_pointer]
            self.top_pointer = self.top_pointer - 1 #Move the pointer      
            return last_element #Pop the last element
        else : 
            return "Underflow"
    def peek(self):
        return self.stack[self.top_pointer]

    def is_empty(self):
        return self.top_pointer == -1
    
    def traverse(self):
        for a in self.stack:
            if a != None:
                print(a,end = " ")
        print()      
    
s = Stack(10)

s.push(20)
s.push(200)
s.push(2000)
s.push(30)
s.push(40)
s.push(20)
s.push(200)
s.push(2000)
s.push(30)
s.push(40)

s.traverse()

s.push(2000)
s.push(2000)
s.push(2000)

print("Top:",s.peek())

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

s.traverse()