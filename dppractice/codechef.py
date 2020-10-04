def findminsubsetsum(arr,row,column):

    dp=[False]*row                  
                                    
    for i in range(row):
        dp[i]=[False]*column
        dp[i][0]=True               
        
    

    for i in range(1,row):          
        for j in range(1,column):    
            if j<arr[i-1]:                          
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    count=0

    
    
    
    for i in dp[row-1][::-1]: 
                                
        if i:
            break
        else:
            count+=2 
    return count,dp
            
k=int(input())
for _ in range(int(input())):

    n=int(input())
    
    arr=[i**k for i in range(1,n+1)]
    
    summ=sum(arr)
    kt=summ//2


    st,dp=findminsubsetsum(arr,n+1,kt+1)
    if 2*kt==summ:                       
        print(st)
        at = (summ-st)//2
        
    elif 2*kt +1==summ:
        print(1+st)
        at = (summ-(1+st))//2
    i=n+1
    j=at
    a=[]
    d=dict()
    for i in range(len(arr)):
        d[arr[i]]=i
    
    a.append(arr[i])
    at-=arr[i]
    j=at
    while i>=0 and j>=0:
        
        if dp[i-1][j]:
            i-=1
        else:
            a.append(arr[i-1])
            j=at-arr[i-1]
            at-=arr[i-1]
        
            
    result = ["0"]*n
    for i in a:
        result[d[i]]="1"
    
    print("".join(result))
        
    
            
    
        
    
