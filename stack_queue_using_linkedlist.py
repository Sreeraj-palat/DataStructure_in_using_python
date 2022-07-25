from re import search


class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class Stack:
    def __init__(self):
        self.head = None


    def push(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.ref = self.head
            self.head = node
    
    def pop(self):
        if self.head is None:
            print("method not possible")
        else:
            self.head = self.head.ref
    
    def stack(self):
        x=self.head
        while x:
            print(x.data,end=",")
            x=x.ref

            

class Queue:

    def __init__(self):
        self.front = None
        self.back = None
    
    def enqueue(self,data):
        node = Node(data)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.ref = node
            self.back =node
    
    def dequeue(self):
        if self.front is None:
            print("not possible")
        else:
            self.front = self.front.ref
        
    def queue(self):
        x=self.front
        while x:
            print(x.data,end=",")
            x=x.ref

    def queuesearch(self):
        data= int(input("enter the number to be searched "))
        if self.front is None:
            print("search not possible")
        else:
            x=self.front
            y=1
            while x:
                if x.data == data:
                    print("item found in "+str(y))
                    break
                x=x.ref
                y=y+1
s=Stack()
q=Queue()


# s.push(10)   
# s.push(1)   
# s.push(14)   
# s.push(15)   
# s.push(12)   
# s.pop()
# s.stack()
    
q.enqueue(9)
q.enqueue(3)
q.enqueue(5)
q.enqueue(8)
q.enqueue(1)
q.enqueue(4)
q.enqueue(6)
# q.dequeue()
# q.queuesearch()
q.queue()