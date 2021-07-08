# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:22:21 2021

@author: DELL
"""

from collections import defaultdict


class Graph:

    def __init__(self):

        self.graph = defaultdict(list)
        #self.cnt2 = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited, cnt):
        visited.add(v)
        ans = 1
        for neighbour in self.graph[v]:
            #print("adjacent",neighbour)
            print("visited", visited)

            if neighbour not in visited:
                print("visiting", neighbour)
                print("cnt", cnt)

                ans += self.DFSUtil(neighbour, visited, cnt + 1)
                print("ans",ans)
        
        return ans

    def DFS(self):
        cost = 0
        visited = set()

        for vertex in list(self.graph):
            if vertex not in visited:
                print("root", vertex)
                
                comp = self.DFSUtil(vertex, visited, 0) - 1
                print("comp", comp)
                
                cost += comp*c_road + c_lib + (n - (comp +1))* c_lib
                print("cost", cost)
        print(cost)


g = Graph()
q = int(input().strip())

for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c_lib = int(first_multiple_input[2])

    c_road = int(first_multiple_input[3])
    for _ in range(m):
        a, b = map(int, input().split())
        g.addEdge(a, b)
    #print(g.graph)
    if c_road > c_lib:
        print(c_lib*n)

    else:
        g.DFS()
