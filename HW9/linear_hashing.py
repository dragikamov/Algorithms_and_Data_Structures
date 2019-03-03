class Node:
    key = ""
    value = ""
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value

    def __ne__(self,other):
        return self.key!=other

    def __eq__(self,other):
        return self.key==other

    def __str__(self):
        return str(self.value)

class HashTable:
    maxSize = 0
    arr = []
    currentSize = 0

    def __init__(self):
        self.maxSize = 5
        for i in range(self.maxSize):
            x = Node()
            self.arr.append(x)
        self.currentSize = 0

    def __str__(self):
        s="Final result:\n"
        for i in range(self.maxSize):
            s += str(self.arr[i]) + " "
        return s

    def hashCode(self,value):
        hashkey = value % 5
        return hashkey
        
    def insert(self,value):
        self.insertNode(self.hashCode(value),value)

    def insertNode(self,key,value):
        self.arr[key].value = value
        self.arr[key].key = key
        self.currentSize += 1

    def get(self,key):
        for i in range(self.maxSize):
            if self.arr[i].key == key:
                return self.arr[i].value
        return None

    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

def main():
    table = HashTable()
    lista = [3, 10, 2, 4]
    for i in lista:
        table.insert(i)
    print(table)

main()
