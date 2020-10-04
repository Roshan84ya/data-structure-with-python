def fibonacciModified(t1, t2, n):
    T=[0]*(n)
    T[0]=t1
    T[1]=t2
    for i in range(2,n):
        T[i]=T[i-2]+(T[i-1])**2
    
    return T[n-1]
    


print(fibonacciModified(0, 1, int(input())))
