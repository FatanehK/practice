class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next= None

class Stack:
    def __init__(self):
        self.top=None
        self.stack_size =0


    def peek(self):
        if self.top :
            return self.top.val
        
        raise ValueError("stack is empty")
    
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.stack_size += 1


    def pop(self):
        if self.top:
            self.stack_size -= 1
            value = self.top.val
            self.top = self.top.next
            return value
        else:
            raise ValueError("Stack is empty")


    def size(self):
        return self.stack_size
stack = Stack()
array =[1,2,3,4,5]
for a in array:
    stack.push(a)
print(stack.size())

for _ in range(len(array)):
    print(stack.pop())