import time
import random

def maxHeap(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        maxHeap(arr, n, largest)

def heapSort(arr):
    for i in range(len(arr), -1, -1):
        maxHeap(arr, len(arr), i)
        
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeap(arr, i, 0)

def main():
    cases=50
    size=150
    int_max=2146483647
    f=open("normal.txt",'w')
    for i in range(cases):
        arr=[0]*size
        f.write(str(size)+"\n")
        for j in range(size):
            arr[j]=int(random.randrange(0,int_max))
        start=time.time()
        heapSort(arr)
        end=time.time()
        f.write(str(end-start)+"\n")
        size+=150
    f.close()

main()
