def length(n):
    k=0
    while n>0:
        n=int(n/10)
        k+=1
    return k

def bucketSort(arr,k):
    buckets=[[] for y in range(10)]
    for i in range(len(arr)):
        index = (arr[i]//k)%10
        buckets[index].append(arr[i])
    for i in range(10):
        if len(buckets[i])>1 and k//10!=0:
            bucketSort(buckets[i],k//10)
    n=0
    for i in range(10):
        for j in range(len(buckets[i])):
            arr[n]=buckets[i][j]
            n+=1
        
def radixSort(arr):
    m=max(arr)
    k=10**(length(m)-1)
    bucketSort(arr,k)
    
    
def main():
    arr=[15,9,3,4,20,5,6,12,9,15]
    radixSort(arr)
    print(arr)
    
main()
