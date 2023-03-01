# list() as a stack
list_stack = []
# push() using append()
list_stack.append(10)
list_stack.append(20)
list_stack.append(30)
# pop() using pop()
print(list_stack.pop())
list_stack.pop()
print(list_stack)
# top() using -ve index
print(list_stack[-1])
print(list_stack)

print("------------------------------")
# ------------------------------------

# stack using list() in OOPS way
class StackList:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)

# ------------------------------------

# stack using single linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class StackLL:
    def __init__(self):
        self.head = None 
    
    def is_empty(self):
        return self.head is None 
    
    def push(self,data):
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.is_empty():
            return 
        else:
            to_delete = self.head
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None 
            del to_delete
            return popped_node.data 
    
    def peek(self):
        if self.is_empty():
            return
        else:
            return self.head.data
    
    def traverse(self):
        final = []
        curr = self.head
        while curr is not None:
            final.append(curr.data)
            curr = curr.next 
        print(final)  
    
sll = StackLL()
sll.push(10)
sll.push(20)
sll.traverse()
print(sll.pop())
print(sll.peek())
sll.traverse()


# ------------------------------------
# Monotonic increasing stack
def monotonic_increasing_stack(array):
    stack = []
    for x in array:
        while stack and stack[-1] > x:
            stack.pop()
        stack.append(x)
    return stack 

print(monotonic_increasing_stack([4,2,5,3,1]))

# Monotonic decreasing stack
def monotonic_decreasing_stack(array):
    stack = []
    for x in array:
        while stack and stack[-1] < x:
            stack.pop()
        stack.append(x)
    return stack 

print(monotonic_decreasing_stack([1,1,3,2,9]))


# ------------------------------------
# Min stack : Retrive minimum element in O(1)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self,item):
        self.stack.append(item)
        if self.min_stack:
           item = item if self.min_stack[-1] > item else self.min_stack[-1]
           self.min_stack.append(item)
        else:
            self.min_stack.append(item)
        
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def get_min(self):
        return self.min_stack[-1]
    
    
ms1 = MinStack()
ms1.push(-10)
ms1.push(0)
ms1.push(10)
ms1.push(-90)
ms1.push(90)
print(ms1.get_min())

# Max stack : Retrieve maximum element in O(1)
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    
    def push(self,item):
        self.stack.append(item)
        if self.max_stack:
           item = item if self.max_stack[-1] < item else self.max_stack[-1]
           self.max_stack.append(item)
        else:
            self.max_stack.append(item)
        
    def pop(self):
        self.stack.pop()
        self.max_stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def get_max(self):
        return self.max_stack[-1]


ms2 = MaxStack()
ms2.push(-10)
ms2.push(0)
ms2.push(10)
ms2.push(-90)
ms2.push(90)
print(ms2.get_max())