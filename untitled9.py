# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 17:09:46 2021

@author: DELL
"""
from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.dist = defaultdict()
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    # Function to print a BFS of graph
    def BFS(self,n, s):
 
        # Mark all the vertices as not visited
        visited = {s}
 
        # Create a queue for BFS
        queue = [s]
        self.dist[s] = 0
        # Mark the source node as
        # visited and enqueue it
        #queue.append(s)
        #visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            node = queue.pop(0)
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            #print(s,self.graph[s])
            for neighbour in self.graph[node]:
                print("node ",node)
                if neighbour not in visited:
                    self.dist[neighbour] = self.dist[node] + 6
                    queue.append(neighbour)
                    visited.add(neighbour)
                    
        res = []
        for i in range(1, n+1):
            if i not in self.dist:
                res.append(-1)
            elif self.dist[i] != 0:
                res.append(self.dist[i])
        print(res)
        
q = int(input().strip())

for q_itr in range(q):
    g = Graph()
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        #edges.append(list(map(int, input().rstrip().split())))
        u, v = map(int, input().rstrip().split())
        g.addEdge(u, v)
    s = int(input().strip())

    result = g.BFS(n,s)
