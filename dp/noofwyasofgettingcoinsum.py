"""def noofways(array,n):
    ways=[0]*(n+1)
    ways[0]=1
    for coin in array:
        for i in (1,n+1):
            if i>=coin:
                ways[i]=ways[i]+ways[i-coin]
    return ways[n]
                


for _ in range(int(input())):
    value=int(input())
    no=int(input())
    coinarray=list(map(int,input().split()))
    noofways(coinarray,value)
"""

for _ in range(int(input())):
    n=int(input())
    kl=list(map(int,input().split()))
    i=0
    count=2
    while i<n:
        print(i)
        jump=kl[i]
        
        if jump==0:
            count=-1
            break
        if len(kl[i+1:i+jump+1])==0:
            print("hey")
            break
        steps=max(kl[i+1:i+jump+1])
        
        
        
        if i+steps+1>=n:
            i+=steps+1
            print("hey1")
            count+=1
            break
            
        i+=steps+1
        count+=1
        
        
    print(count,i)
            
        
        
        
 
        
            
        
        
        
 
        
            
        
        
        
 
        
