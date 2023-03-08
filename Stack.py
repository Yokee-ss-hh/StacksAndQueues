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

# ------------------------------------
# Infix To Prefix
#  Step 1: First reverse the given expression 
#  Step 2: If the scanned character is an operand, put it into prefix expression.
#  Step 3: If the scanned character is an operator and operator's stack is empty, push operator into operators' stack.
#  Step 4: 
#      If the operator's stack is not empty, there may be following possibilities.
#      If the precedence of scanned operator is greater than the top most operator of operator's stack, push this operator into operator 's stack.
#      If the precedence of scanned operator is less than the top most operator of operator's stack, pop the operators from operator's stack untill we find a low precedence operator than the scanned character. 
#      If the precedence of scanned operator is equal then check the associativity of the operator. If associativity left to right then simply put into stack. If associativity right to left then pop the operators from stack until we find a low precedence operator.
#      If the scanned character is opening round bracket ( '(' ), push it into operator's stack.
#      If the scanned character is closing round bracket ( ')' ), pop out operators from operator's stack until we find an opening bracket ('(' ).
#  Repeat Step 2,3 and 4 till expression has character 
#  Step 5: Now pop out all the remaining operators from the operator's stack and push into postfix expression.
#  Step 6: Exit

def infix_to_prefix(expression): 
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = [] # initialization of empty stack
    output = ''
    rev_exp = ""
    for x in expression:
        if x == '(':
            rev_exp = ')'+rev_exp
        elif x == ')':
            rev_exp = '('+rev_exp
        else:
            rev_exp = x + rev_exp
    for character in rev_exp:
        if character not in operators:  # if an operand append in postfix expression
            output+= character
        elif character=='(':  # else Operators push onto stack
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else: 
            while stack and stack[-1]!='(' and priority[character]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output[::-1]

print(infix_to_prefix("m*n+(p-q)+r"))

# +*mn+-pqr


def infix_to_postfix(expression): 
    
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = [] # initialization of empty stack
    output = ''
    for character in expression:
        if character not in operators:  # if an operand append in postfix expression
            output+= character
        elif character=='(':  # else Operators push onto stack
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else: 
            while stack and stack[-1]!='(' and priority[character]<=priority[stack[-1]]:
                output+=stack.pop()
            stack.append(character)
    while stack:
        output+=stack.pop()
    return output
        
print(infix_to_postfix("m*n+(p-q)+r"))



def prefix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    for x in expression[::-1]:
        if x not in operators:
            stack.append(x)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append("("+op1+x+op2+")")
    return stack[0]

print(prefix_to_infix("+*mn+-pqr")) 


def postfix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    for x in expression:
        if x not in operators:
            stack.append(x)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append("("+op2+x+op1+")")
    return stack[0]

print(postfix_to_infix("mn*pq-+r+"))


def prefix_to_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    for x in expression[::-1]:
        if x not in operators:
            stack.append(x)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1+op2+x)
    return stack[0]

print(prefix_to_postfix("+*mn+-pqr"))


def postfix_to_prefix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '(', ')', '^'])
    for x in expression:
        if x not in operators:
            stack.append(x)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(x+op2+op1)
    return stack[0]

print(postfix_to_prefix("mn*pq-+r+"))
    
    
    
    
    