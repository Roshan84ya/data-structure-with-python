"""
conversting string s1 into s2

here is my approcah here we will calculate the longest matching subsequesnce lenght
and we substract it from the kength of longest string



"""

for _ in range(int(input())): #test case
    n,m=map(int,input().split()) #lenght of both the string

    str1,str2=input().split()

    arr=[0]*(m+1)
    for i in range(m+1):
        arr[i]=[0]*(n+1)



        
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                
                arr[i][j]=j #i== 0  means we dont have element in the first string so we need to add j element
            elif j==0:      #if j==0 means we dont have element in the second string so we need to remove i element from the first string
                arr[i][j]=i
            elif str2[i-1]==str1[j-1]:        #here if match is found then so even adding this eleemtn will not effect the previous minimum that is at arr[i-1][j-1](not taking these element)
                
                arr[i][j]=arr[i-1][j-1]
            else:
                arr[i][j]=1+min(arr[i-1][j-1], #not taking last elemetn
                              arr[i-1][j],      #remove
                              arr[i][j-1])      #insert

    print(arr[-1][-1])
