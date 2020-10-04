"""
Range sum queries

"""
arr=[10,20,30,40,50]

arrn=[0]*5
sum1=0
for i in range(5):
    sum1+=arr[i]
    arrn[i]=sum1
print(arrn)
n=int(input()) # n query
for i in range(n):
    kt=input("for update type u and for sum type s\n")
    if kt=="s":
        a,b=map(int,input().split())
        if a==0:
            print(arrn[b])
        else:
            print(arrn[b]-arrn[a-1])
    elif kt=="u":
        a,b=map(int,input().split())
        rs=b-arr[i]
        for i in range(1,n):
            arrn[i]=arrn[i]+40
