def partition(arr, start, end):
    if arr[start]>arr[end]:
       arr[start],arr[end] = arr[end],arr[start]
    s=start+1
    e=end-1
    curr=start+1
    p=arr[start]
    q=arr[end]
    while curr<=e:
        if arr[curr]<p:
            arr[curr],arr[s] = arr[s],arr[curr]
            s+=1
        elif arr[curr]>=q:
            while arr[e]>q and curr<e:
                e-=1
            arr[curr],arr[e] = arr[e],arr[curr]
            e-=1
            if arr[curr]<p:
                arr[curr],arr[s] = arr[s],arr[curr]
                s+=1
        curr+=1
    s-=1
    e+=1
    arr[start],arr[s] = arr[s],arr[start]
    arr[end],arr[e] = arr[e],arr[end]
    return s,e

def quicksort(arr, start, end):
    if(start<end):
        arr[start+1],arr[end] = arr[end],arr[start+1]
        lp,rp=partition(arr,start,end)
        quicksort(arr,start,lp-1)
        quicksort(arr,lp+1,rp-1)
        quicksort(arr,rp+1,end)

def main():
    arr=[6,10,13,5,8,3,2,11]
    quicksort(arr,0,len(arr)-1)
    print(arr)

main()
