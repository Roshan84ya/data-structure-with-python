def platessum(arr,p,n):
    dp=[0]*(n)
    for i in range(n):
        dp[i]=[0]*(p)
    
    for i in range(1,p):
        dp[0][i]=sum(subsum[0][:i])
                     
    
    print(dp)
    for i in range(1,n):
        for j in range(,p):
            for x in range(0,min(j,k)+1):
                
                print(dp[i-1][(j-x)],sum(subsum[i][:x+1]))
                dp[i][j]=max(dp[i][j],sum(subsum[i][:x+1])+dp[i-1][j-x])
                
                
    print(dp)
    
    
    
    


for i in range(int(input())):
    
    n,k,p=map(int,input().split())
    subsum=[0]*n
    for ijk in range(n):
        a=list(map(int,input().split()))
        subsum[ijk]=a[:k]
    platessum(subsum,p,n)
    
    
