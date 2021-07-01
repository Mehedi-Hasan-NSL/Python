# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 08:24:29 2021

@author: DELL
"""


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, data):
        a = Node(data)
        self.head = a

def traversal(l):
    temp = l.head #temporary pointer to point to head

    a = ''
    while temp != None: #iterating over linked list
      a = a+str(temp.data)+'\t'
      temp = temp.next

    print(a)

def insert_at_beginning(l, n):
    n.next = l.head
    l.head = n

def insert_at_last(l, n):
    temp = l.head
    
    while temp.next != None:
      temp = temp.next
    
    temp.next = n

def insert_node_after(n, a):
    n.next = a.next
    a.next = n

def delete(l, n):
    temp = l.head
    if temp == n: #node to be deleted is head
      l.head = n.next
      del n
    else: #node to be deleted is not head
      while temp != None:
        if temp.next == n: #node previous to node to be deleted
          temp.next = n.next
          del n
          break #breaking the loop after deleting the node
        temp = temp.next

if __name__ == '__main__':
    l = LinkedList(10)
    
    a = Node(20)
    b = Node(50)
    c = Node(60)
    

    
    l.head.next = a
    a.next = b
    b.next = c
    
    traversal(l)
    
    z = Node(0)
    insert_at_beginning(l, z)
    z = Node(-10)
    insert_at_beginning(l, z)
    
    z = Node(100)
    insert_at_last(l, z)
    
    z = Node(30)
    insert_node_after(z, a)
    z = Node(40)
    insert_node_after(z, a.next)
    z = Node(500)
    insert_node_after(z, a.next.next)
    
    traversal(l)
    
    delete(l, l.head)
    delete(l, z)
    
    traversal(l)
