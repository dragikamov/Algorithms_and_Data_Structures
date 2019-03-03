from math import sqrt
import timeit

#Naive
def Fibonacci(n):
    if (n==1 or n==2):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

#Bottom up
def fib(n):
    if(n==1 or n==2):
        return 1
    f1=1
    f2=1
    f3=0
    for i in range(3,n+1):
        f3=f1+f2
        if(i!=n):
            f1=f2
            f2=f3
    return f3

#Closed-form
def fi(n):
    gr=(1.0+sqrt(5.0))/2.0
    return round((gr**n)/sqrt(5.0))

#Matrix representation
def multiply(F,M):
    x=F[0]*M[0]+F[1]*M[2]
    y=F[0]*M[1]+F[1]*M[3]
    z=F[2]*M[0]+F[3]*M[2]
    w=F[2]*M[1]+F[3]*M[3]
    F[0]=x
    F[1]=y
    F[2]=z
    F[3]=w
    return F

def power(F,n):
    M=[1,1,1,0]
    for i in range(2,n+1):
        F=multiply(F,M)
    return F

def f(n):
    F=[1,1,1,0]
    if(n==0):
        return 0
    F=power(F,n-1)
    return F[0]

def main():
    n=1
    file=open("matrix_python.txt",'w')
    while True:
        start=timeit.default_timer()
        res=f(n)
        end=timeit.default_timer()
        if((end-start)>=5):
            break
        elif(res<0 or n>100):
            break
        else:
            file.write(str(n)+" "+str(res)+"\n")
            file.write(str(end-start)+"\n")
            n=n+1
    file.close()

    n=1
    file=open("closed_python.txt",'w')
    while True:
        start=timeit.default_timer()
        res=fi(n)
        end=timeit.default_timer()
        if((end-start)>=5):
            break
        elif(res<0 or n>100):
            break
        else:
            #print(n,res)
            #print(end-start,"\n")
            file.write(str(n)+" "+str(res)+"\n")
            file.write(str(end-start)+"\n")
            n=n+1
    file.close()

    n=1
    file=open("bottom_python.txt",'w')
    while True:
        start=timeit.default_timer()
        res=fib(n)
        end=timeit.default_timer()
        if((end-start)>=5):
            break
        elif(res<0 or n>100):
            break
        else:
            #print(n,res)
            #print(end-start,"\n")
            file.write(str(n)+" "+str(res)+"\n")
            file.write(str(end-start)+"\n")
            n=n+1
    file.close()

    n=1
    file=open("naive_python.txt",'w')
    while True:
        start=timeit.default_timer()
        res=Fibonacci(n)
        end=timeit.default_timer()
        if((end-start)>=5):
            break
        elif(res<0 or n>100):
            break
        else:
            #print(n,res)
            #print(end-start,"\n")
            file.write(str(n)+" "+str(res)+"\n")
            file.write(str(end-start)+"\n")
            n=n+1
    file.close()

main()
