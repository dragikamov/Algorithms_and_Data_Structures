class StackNode(object):
    data=""
    next=None

class Stack(object):
    top=StackNode()
    size=-1
    current_size=-1
    def push(self, val):
        if self.size>0 and self.current_size<self.size:
            new=StackNode()
            new.data=val
            new.next=self.top
            self.top=new
            self.current_size+=1
    def pop(self):
        if self.current_size>=0:
            self.current_size-=1
            curr=self.top
            self.top=self.top.next
            return curr.data
    def isEmpty(self):
        if self.current_size==-1 or self.current_size==0:
            return True
        else:
            return False
    def __init__(self, size=0):
        self.size=size
        self.current_size=0
