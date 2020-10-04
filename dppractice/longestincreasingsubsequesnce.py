"""
5 8 3 7 9 1
5

8
1 2
3
1 2 1
1 2 1 2
1 2 1 2 3
1

"""
for _ in range(int(input())): #Test_cases

    n=int(input()) #number_of_input
    arr=list(map(int,input().split())) #liist

    maxm=1 #counter of maximum increasing subsequesnce
    arrmaxx=[1]*n #the array in which we store the maximum of each step

    for i in range(n): #iterating through each index
        for j in range(i): #iteration to the index less than i and we are interested in finding the numbers that are smaller than the arr[i]
            if arr[i]>arr[j] and arrmaxx[i]<arrmaxx[j]+1:
                arrmaxx[i]=arrmaxx[j]+1
                maxm=max(arrmaxx[i],maxm)
    print(maxm)
    
    
    
