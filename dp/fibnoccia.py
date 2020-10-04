dp=[0]*100

def fib(n):
    if dp[n]>0:
        return dp[n]
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
        
for _ in range(int(input())):
    dp[0]=0
    dp[1]=1
    dp[2]=1
    n=int(input())
    print(fib(n))
    
