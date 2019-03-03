def l_o_s(arr):
    n = len(arr)
    P = [0] * n
    M = [0] * (n+1)
    L = 0
    for i in range(n):
       lo = 1
       hi = L
       while lo <= hi:
           mid = (lo+hi)//2
           if (arr[M[mid]] < arr[i]):
               lo = mid+1
           else:
               hi = mid-1
 
       newL = lo
       P[i] = M[newL-1]
       M[newL] = i
 
       if (newL > L):
           L = newL
 
    S = []
    k = M[L]
    for i in range(L-1, -1, -1):
        S.append(arr[k])
        k = P[k]
    return S[::-1]
 
def main():
    A=[8,3,6,50,10,8,100,30,60,40,80]
    print(A)
    print(l_o_s(A))

main()
