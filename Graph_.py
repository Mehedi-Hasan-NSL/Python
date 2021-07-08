# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:04:18 2021

@author: DELL
"""

#from python.basic import Graph


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) >= 1:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

    def display(self):
        print(*self.queue)


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.pred = None
        self.distance = 0
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
        
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getPred(self):
        return self.pred

    def setPred(self, pred):
        self.pred = pred
        
    def getDistance(self):
        return self.distance 
    def setDistance(self, distance):
        self.distance = distance

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    #print("q",vertQueue.display())
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        #print("size",vertQueue.size())
        print(currentVert.getId()," ",currentVert.getDistance())
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')



g = Graph()
for i in range(6):
    g.addVertex(i)
print(*g.getVertices())

g.addEdge(0, 1)
g.addEdge(0, 5)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 0)
g.addEdge(5, 4)
g.addEdge(5, 2)


root = g.getVertex(0)
bfs(g,root)






"""
g = Graph()
for i in range(6):
    g.addVertex(i)
print(*g.getVertices())

g.addEdge(0, 1)
g.addEdge(0, 5)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 0)
g.addEdge(5, 4)
g.addEdge(5, 2)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
        
"""
