class Node:
    def __init__(self,data=None):
        self.data = data
        self.ref = None

class Ll:

    def __init__(self):
        self.head = None
        # /new_node = Node(data)
    def add_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while(n.ref != None):
                n = n.ref
            
            n.ref = new_node
    def trav(self):
        if self.head is None:
            print("the list is empty")
        else:
            n = self.head
            while(n != None):
                print(n.data)
                n = n.ref
    def reverse(self):
        if self.head is None:
            print("the list is empty")
        else:
            p = None
            while(self.head != None):
                n = self.head.ref
                self.head.ref = p
                p = self.head
                self.head = n
            self.head = p




    
        
x = Ll()
x.add_beg(6)
# x.add_beg(67)
# x.add_beg()
# x.add_end(90)
# x.add_end(99)
# x.reverse()

x.trav()