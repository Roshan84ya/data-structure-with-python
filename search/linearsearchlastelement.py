n,k=map(int,input().split())
f=-1
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]==k:
        f=i+1
print(f)
