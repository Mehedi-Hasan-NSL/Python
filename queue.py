class Queue:

    def __init__(self, size):
      self.head = 1    # head and tail both 1
      self.tail = 1
      self.Q = [0]*(size)
      self.size = size

    def is_empty(self):
      if self.tail == self.head:
        return True
      return False

    def is_full(self):
      if self.head == (self.tail+1) % self.size:
        return True
      return False

    def enqueue(self, x):
      if self.is_full(): 
        print("Queue Overflow",x)
      else:
        #print("b",self.tail)
        #print("b",self.size)
        
        if self.tail + 1 == self.size:    
          self.tail = 1        
        else:
          self.tail = self.tail+1
        self.Q[self.tail] = x
    def dequeue(self):
      if self.is_empty():
        print("Underflow")
      else:
        x = self.Q[self.head]
        if self.head == self.size:
          self.head = 1
        else:
          self.head = self.head+1
        return x

    def display(self):
      i = self.head
     
      if (i > self.tail):
          while(i < self.size):
              print(i," ",self.Q[i])
              i = i+1
          for j in range(1,self.tail+1):
              print(j," ",self.Q[j])
      while(i < self.tail):
        print(self.Q[i])
        if(i == self.size):
          i = 0
        i = i+1


if __name__ == '__main__':
    q = Queue(10)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.display()

    print("")

    q.dequeue()
    q.dequeue()
    q.display()

    print("")

    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(160)
    q.enqueue(170)
    q.enqueue(260)
    q.enqueue(80)
    q.enqueue(90)
    
    print("")
    q.display()
    
    print("")
    q.dequeue()
    q.dequeue()
    q.display()
    
    q.enqueue(80)
    q.enqueue(90)
    
    print("")
    q.display()