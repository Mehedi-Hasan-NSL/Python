# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 08:29:38 2021

@author: DELL
"""


class Node():


    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None


class LinkedList():


    def __init__(self, data):
      a = Node(data)
      self.head = a


def traversal(l):


    temp = l.head  # temporary pointer to point to head
    
    a = ''
    while temp != None:  # iterating over linked list
      a = a+str(temp.data)+'\t'
      temp = temp.next
    
    print(a)


def insert_at_front(l, n):


    n.next = l.head
    l.head.prev = n
    l.head = n


def insert_at_tail(l, n):

    
    temp = l.head
    
    while temp.next != None:
      temp = temp.next
    
    temp.next = n
    n.prev = temp


def insert_after(n, a):


    n.next = a.next
    a.next.prev = n
    a.next = n
    n.prev = a


def delete(l, a):

    
    if a.prev != None:  # node is not head
      a.prev.next = a.next
    else:  # node a is head
      l.head = a.next
    
    if a.next != None:
      a.next.prev = a.prev
    del a

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
    insert_at_front(l, z)
    z = Node(-10)
    insert_at_front(l, z)
    
    z = Node(100)
    insert_at_tail(l, z)
    
    z = Node(30)
    insert_after(z, a)
    z = Node(40)
    insert_after(z, a.next)
    z = Node(500)
    insert_after(z, a.next.next)
    
    traversal(l)
    
    delete(l, l.head)
    delete(l, z)

traversal(l)
