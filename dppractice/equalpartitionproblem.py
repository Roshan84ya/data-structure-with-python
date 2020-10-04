
"""
equal partition subset sum problem

"""
def findsubsetsum(arr,column,row):
    dp=[False]*row
    for i in range(row):
        dp[i]=[False]*column
        dp[i][0]=True

    for i in range(1,row):
        for j in range(1,column):
            if j<arr[i-1]: #if sum is smaller than the current number then we cant take it as it can't help in attaing the sum that os smaller than this number
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    if dp[-1][-1]:
        return "YES"
    return "NO"
    
for _ in range(int(input())): #Test cse
    n=int(input())          #Total number of element in the array
    arr=list(map(int,input().split())) # numbers in the array
    k=sum(arr)
    if k%2!=0:
        print("NO")
    else:
        print(findsubsetsum(arr,(k//2)+1,n+1))
    
