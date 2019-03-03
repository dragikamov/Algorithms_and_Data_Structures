class binNode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key_node):
    if root==None:
        root=key_node
    else:
        if root.val<key_node.val:
            if root.right==None:
                root.right=key_node
            else:
                insert(root.right,key_node)
        else:
            if root.left==None:
                root.left=key_node
            else:
                insert(root.left,key_node)
 
def inorder(x,root):
    if root:
        inorder(x,root.right)
        x.push(root.val)
        inorder(x,root.left)

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
            new.data=val
            new.next=self.first
            self.first=new
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
        print("Printing Linked List:")
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

def main():
    y= binNode(5)
    insert(y,binNode(3))
    insert(y,binNode(2))
    insert(y,binNode(4))
    insert(y,binNode(7))
    insert(y,binNode(6))
    insert(y,binNode(8))

    x=LinkedList(7)

    inorder(x,y)

    x.print()

main()
