class Node(object):
    data=""
    next=None

class LinkedList(object):
    first=Node()
    size=-1
    current_size=-1
    def push(self, val):
        if self.size>0 and self.current_size==0:
            self.first.data=val
            self.current_size+=1
        elif self.size>0 and self.current_size<self.size:
            new=Node()
            cursor=self.first
            new.data=val
            while cursor.next!=None:
                cursor=cursor.next
            cursor.next=new
            self.current_size+=1
        else:
            print("The list is full!")
    def pop(self):
        if self.current_size>=0:
            cursor=self.first
            for n in range(self.current_size-1):
                cursor=cursor.next
            self.current_size-=1
            return cursor.data
        else:
            print("Error popping element")
    def print(self):
        if self.isEmpty==True:
            print("The list is empty!")
        else:
            cursor=self.first
            for n in range(self.current_size):
                print(cursor.data," ",sep="",end="")
                cursor=cursor.next
    def isEmpty(self):
        if self.current_size==-1 or self.current_size==0:
            return True
        else:
            return False
    def __init__(self, size=0):
        self.size=size
        self.current_size=0
    def reverse(self):
        prev=self.first
        curr=prev.next
        ne=curr.next
        prev.next=None
        for n in range(self.current_size-1):
            curr.next=prev
            prev=curr
            curr=ne
            if ne.next!=None:
                ne=ne.next
        self.first=prev
