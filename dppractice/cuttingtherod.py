"""
in this n segments are give and you need to find the maximum cut of the segment i.e
at the end the legth of the rod is 0 and we have the maximum number of segment


"""

for _ in range(int(input())):
    rod=int(input())
    arr=list(map(int,input().split()))


    dp=[0]*(rod+1)
    

    for i in arr:
        for j in range(1,rod+1):
            if j==i:              #if we have the sting legth is equal to current cut the we will check whether it is greater than the current or 1
                dp[j]=max(dp[j],1)
            elif j>i and dp[j-i]: # we will i=obly cionsider the cut if we have j-i is non 0 i.e we can get those cut by other cut or by this cut also
                dp[j]=max(dp[j],dp[j-i]+1)
                
                
    print(dp[-1])

        
