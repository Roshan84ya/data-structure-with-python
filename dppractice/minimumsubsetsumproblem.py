def findminsubsetsum(arr,row,column):

    dp=[False]*row                  # here we are making the array of True and false and putting the sum at the column and number of elelent at the row if certain sum will be achievable
                                    # than we will mark it as a true or else we will mark it as a false
    for i in range(row):
        dp[i]=[False]*column
        dp[i][0]=True               # here we are making the sum==0 Always true because it can be acheived alsways as the sum of empty subset is 0 and empty subset is the subset of every set
        
    

    for i in range(1,row):          #here we are iterating over the element of the array each time we will pick the certain element and we will find if the sumof this element is possible or not
        for j in range(1,column):   #here we are calulating sum if j= sum 
            if j<arr[i-1]:          #if sum is samller then the current eleemnt then ofcourse well not take that element and hence we will print we are not taking this element byproviding the previous value
                
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    count=0
    #for i in dp:
        #print(*i)
    
    for i in dp[row-1][::-1]: #here i'm itrating over the last column i.e if we fond the true at the irst index then we return 0 or else we 'll keep incrementinh count by 2 as we are calculating the
                                #fiffereance so if i move i in the last row the difference will become 2 ex if i have a number 56 28 28 else 27 and 29 see by moving 1 we have difference of two
        if i:
            break
        else:
            count+=2 
    return count
            

for _ in range(int(input())): #TEst Case

    n=int(input()) #size of array
    arr=list(map(int,input().split())) #array

    summ=sum(arr)
    k=summ//2


    st=findminsubsetsum(arr,n+1,k+1)
    if 2*k==summ:                       # here again we need to work if our k is half of sum the well print just count but if our summ is odd if we divide it into two half so initially we are taking the difference of 1
        print(st)
    elif 2*k +1==summ:
        print(1+st)
        
    
