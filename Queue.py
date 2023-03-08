from collections import deque


# queue using list 
my_queue = list()
# enqueue() using append()
my_queue.append(10)
my_queue.append(20)
my_queue.append(30)
# dequeue() using pop(0)
print(my_queue.pop(0))
print(my_queue.pop(0))
print(my_queue)
# peek() using index 0 
print(my_queue[0])

print("-----------------------")
# ----------------------------
# simple queue using list() in OOP way
class QueueList:
    def __init__(self,size):
        self.queue = [] 
        self.count = 0 
        self.size = size 
    
    def enqueue(self,item):
        if self.is_full():
            raise Exception("Queue is full")
        else:
            self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return self.size == len(self.queue)
    
    def peek(self):
        if not self.count == 0:
            return self.queue[0]


print("-----------------------")
# ----------------------------
# simple queue using linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        
class QueueLL:
 
    def __init__(self):
        self.front = self.rear = None
        self.count = 0
 
    def isEmpty(self):
        return self.front == None
 
    def enqueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return
        else:
           self.rear.next = temp
           self.rear = temp

    def dequeue(self):
        if self.isEmpty():
            return
        else:
           temp = self.front
           self.front = temp.next
        if(self.front == None):
            self.rear = None

print("-----------------------")
# ----------------------------
# Circular Queue using list()
class CirQueue:
    def __init__(self,size):
        self.queue = [-1]*size
        self.size = size
        self.front = self.rear = -1
    
    def enqueue(self,item):
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0 
            self.queue[self.front] = item 
        elif self.is_full():
            raise Exception("Queue is full")
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = item 
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.front == self.rear:
            to_be_returned = self.queue[self.front]
            self.front = 0
            self.rear = 0
            return to_be_returned
        else:
            to_be_returned = self.queue[self.front]
            self.front = (self.front+1) % self.size
            return to_be_returned
    
    def display(self):
        final_array = []
        x = self.front
        y = self.rear
        if x == -1 and y == -1:
            raise Exception("No items in the queue")
        elif x == y:
            final_array.append(self.queue[self.front])
        elif y > x:
            for z in range(x, y+1):
                final_array.append(self.queue[z])
        else:
            for i in range(x,self.size):
                final_array.append(self.queue[i])
            for j in range(0,y+1):
                final_array.append(self.queue[j])
        return final_array
                
    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
    
    def is_full(self):
        return (self.rear+1) % self.size == self.front 
    
    def is_empty(self):
        return (self.front == -1 and self.rear == -1)



print("----------Max priority queue using list()-------------")
# ----------------------------
employees1 = []
employees1.append((1, "Andrew"))
employees1.append((4, "John"))
employees1.sort()
employees1.append((3, "Jean"))
employees1.sort()
employees1.append((2, "Matt"))
employees1.sort()
while employees1:
    print(employees1.pop())

print("----------Min priority queue using list()-------------")
# ----------------------------
employees2 = []
employees2.append((1, "Andrew"))
employees2.append((4, "John"))
employees2.sort(reverse=True)
employees2.append((3, "Jean"))
employees2.sort(reverse=True)
employees2.append((2, "Matt"))
employees2.sort(reverse=True)
while employees2:
    print(employees2.pop())
    
print("----------Max priority queue using list() and OOPS-------------")
# ---------------------------- 
# Priority Queue using list() and OOPS
# An element with high priority is dequeued before an element with low priority.
# If two elements have the same priority, they are served according to their order in the queue.
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,priority,data):
        self.queue.append((priority,data))
    
    def dequeue(self):
        if self.queue:
            maximum = float('-inf')
            for i in range(len(self.queue)):
               if self.queue[i][0] > maximum:
                   maximum = i
            to_pop = self.queue[maximum][1]
            del self.queue[maximum]
            return to_pop
        else:
            raise Exception("Queue is empty")

pq = PriorityQueue()
pq.enqueue(-20,"yokesh")
pq.enqueue(10,"hello")
pq.enqueue(44,"holi")
pq.enqueue(66,"ocean")
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())


print("----------Min priority queue using list() and OOPS-------------")
# ---------------------------- 
# Priority Queue using list() and OOPS
# An element with low priority is dequeued before an element with high priority.
# If two elements have the same priority, they are served according to their order in the queue.
class PriorityQueue1:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,priority,data):
        self.queue.append((priority,data))
    
    def dequeue(self):
        if self.queue:
            minimum = float('inf')
            for i in range(len(self.queue)):
               if self.queue[i][0] < minimum:
                   minimum = i
            to_pop = self.queue[minimum][1]
            del self.queue[minimum]
            return to_pop
        else:
            raise Exception("Queue is empty")

pq1 = PriorityQueue1()
pq1.enqueue(-20,"yokesh")
pq1.enqueue(10,"hello")
pq1.enqueue(44,"holi")
pq1.enqueue(66,"ocean")
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())
print(pq1.dequeue())

#------------------------------
# ---------priority queue using heapq---------
# Generally, heapq module provides Min Heap implementation of priority queue, But we can use this implementation in 2 ways to create Max priority queue
print("----------Min priority queue using heapq-------------")
import heapq

li1 = [13,2,10,66]
heapq.heappush(li1,999)
heapq.heappush(li1,1)
heapq.heappush(li1,-10)
# After adding above 2 items, No need to do heapify them, heapq does internally
print(heapq.heappop(li1))
print(heapq.heappop(li1))
print(heapq.heappop(li1))
print(heapq.heappop(li1))
print(heapq.heappop(li1))
print(heapq.heappop(li1))


print("----------Max priority queue using heapq-------------")
li2 = [13,2,10,66]
heapq.heappush(li2,-2)
heapq.heappush(li2,-23)
heapq._heapify_max(li2)
# After adding above 2 items, No need to do heapify them, heapq does not do max heapify internally
print(heapq._heappop_max(li2))
print(heapq._heappop_max(li2))
print(heapq._heappop_max(li2))
print(heapq._heappop_max(li2))
print(heapq._heappop_max(li2))
print(heapq._heappop_max(li2))




