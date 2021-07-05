# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 15:52:06 2021

@author: DELL
"""

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

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

def isBalanced(s):
    # Write your code here
    mystack=Stack(len(s))
    if s=="":
        return "Yes"
    for c in s:
        
        if c=="(" or c=="[" or c == "{": 
            mystack.push(c) #push the opening bracket
        else:
            if mystack.is_empty(): 
                return "No"
            if c==")" and mystack.peek()!="(": #the brackets dont matchs
                return "No"
            
            if c=="}" and mystack.peek()!="{": #the brackets dont match
                return "No"

            if c=="]" and mystack.peek()!="[": #the brackets dont matchs
                return "No"
            mystack.pop() #pop matching brackets
    
           
    if mystack.is_empty(): #stack must be empty at the end
        return 'Yes'
    return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') 

    t = int(input().strip())    

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()


#print(checkBalance("([()[]()])()"))
#print(checkBalance("(([()])))"))