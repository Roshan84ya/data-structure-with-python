"""

here we have to find the length of smalllest string that will consist both the string subsequence
"""


for _ in range(int(input())):
    str1,str2=input().split()
    row=len(str1)
    column=len(str2)
    dp=[0]*(row+1)
    for i in range(row+1):
        dp[i]=[0]*(column+1)

    for i in range(1,row+1):
        for j in range(1,column+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(row+column-dp[-1][-1])
                
                
        
