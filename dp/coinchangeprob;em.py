def getWays(n, c):
    subsum=[0]*(len(c)+1)
    
    for i in range(len(subsum)):
        subsum[i]=[0]*(n+1)
    for i in range(len(subsum)):
        subsum[i][0]=1

    for i in range(1,len(c)+1):
        for j in range(1,n+1):
            if n<c[i-1]:
                subsum[i][j]=subsum[i-1][j]
            else:
                while n>=c[i-1]:
                    subsum[i][j]=subsum[i-1][j-c[i-1]] + subsum[i-1][j]
                    n=n-subsum[i-1][j-c[i-1]] + subsum[i-1][j]
            
                subsum[i][j]=subsum[i-1][j-c[i-1]] + subsum[i-1][j]
                

    print(subsum)
                
    


n,c=map(int,input().split())
c=list(map(int,input().split()))
print(getWays(n, c))    

