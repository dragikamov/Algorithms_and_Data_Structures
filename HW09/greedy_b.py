class Activities:
    start = 0
    end = 0
    taken = 0
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.taken = 0

    def __str__(self):
        return "Start: " + str(self.start) + " End: " + str(self.end)

    def __le__(self,other):
        return self.end <= other.start

    def __ge__(self,other):
        return self.start >= other.start

def hashing(arr):
    n = len(arr)
    last = -1
    for i in range(n):
        max_idx = -1
        for j in range(n):
            if arr[j].taken == 1:
                continue
            if last == -1:
                if max_idx == -1:
                    max_idx = j
                elif arr[j] >= arr[max_idx]:
                    max_idx = j
            else:
                if max_idx == -1 and arr[j] <= arr[last]:
                    max_idx = j
                elif arr[j] >= arr[max_idx] and arr[j] <= arr[last]:
                    max_idx = j
        if max_idx == -1:
            break
        else:
            arr[max_idx].taken = 1
            last = max_idx

    res = []
    for i in arr:
        if i.taken == 1:
            res.append(i)
    return res


def main():
    arr = []
    n = int(input("Enter the number of activities: "))
    for i in range(n):
        if i == 0 or i == 20:
            print("\n",i+1,"st activity:",sep="")
        else:
            print("\n",i+1,"th activity:",sep="")
        s = int(input("Enter start time: "))
        e = int(input("Enter end time: "))
        arr.append(Activities(s, e))
    
    print("\nSolution:")
    res = hashing(arr)
    for i in res:
        print(i)
    print("The solution is consisted of ",len(res)," activities.",sep="")
    
main()
