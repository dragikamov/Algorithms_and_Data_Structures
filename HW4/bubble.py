import random
import time

# The bubble sort goes to the end and while going it
# is sorting. So only the last element is going to
# be in its final position.
def bubbleSort(arr):
    n = len(arr)
    # This is the loop repeating as much as there are
    # elements in the array.
    for i in range(n-1):
        noSwap=True
        # This is the loop that goes through the array
        # to the end of the array. And the ending of
        # the array is lowering for every step because
        # we have set the last element.
        for j in range(0, n-i-1):
            # Cheking if the element is bigger than the
            # next one.
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # I have a boolean value because I want
                # to check if the array is already sorted.
                noSwap=False
        # And if the array is already sorted I am stopping
        # the sort.
        if noSwap==True:
            break

def main():
    cases=50
    size=150
    int_max=2146483647
    f=open("bubble.txt",'w')
    for i in range(cases):
        arr=[0]*size
        f.write(str(size)+"\n")
        for j in range(size):
            arr[j]=int(random.randrange(0,int_max))
        start=time.time()
        bubbleSort(arr)
        end=time.time()
        f.write(str(end-start)+"\n")
        size+=150
    f.close()

main()
