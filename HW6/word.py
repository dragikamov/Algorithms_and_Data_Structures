class Node(object):
    val=""
    next=None

class LinkedList(object):
    def push(self,curr,val):
        if curr.val > val:
            newNode=Node()
            newNode.val=curr.val
            newNode.next=curr.next
            curr.val=val
            curr.next=newNode
        else:
            prev=Node()
            prev=curr
            while curr!=None and curr.val<val:
                prev=curr
                curr=curr.next
            newNode=Node()
            newNode.val=val
            newNode.next=curr
            prev.next=newNode
    start=Node()
    start=None
    def insert(self,val):
        if self.start==None:
            self.start=Node()
            self.start.val=val
            self.start.next=None
        else:
            self.push(self.start,val)
    def read(self,output):
        curr=Node()
        curr=self.start
        while curr!=None:
            output.append(curr.val)
            curr=curr.next
        return output

def mysort(a):
    lista=[]
    for i in range(26):
        x=LinkedList()
        lista.append(x)
    for i in range(len(a)):
        idx=int(ord(a[i][0])-97)
        lista[idx].insert(a[i])
    output=[]
    for i in range(26):
        output=lista[i].read(output)
    a=output
    return a

def main():
    n=int(input("Enter the number of words to be entered\n"))
    a=[]
    k=int(input("Enter the length of the words to be entered\n"))
    for i in range(n):
        tmp=""
        tmp=input("Enter words of equal length {:} ".format(k))
        while len(tmp)!=k:
            print("Invalid input, enter a word of lenght ",k,end="")
            tmp=input()
        a.append(tmp)
    a=mysort(a)
    print(a)

main()
