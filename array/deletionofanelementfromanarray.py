#deletionofanelementfromtheararay
arr=[3,8,12,5,6]
n=int(input())
k=-1
for i in range(len(arr)):
    if arr[i]==n:
        k=i
for i in range(k+1,len(arr)):
    arr[i-1]=arr[i]
if k!=(-1):
    del arr[-1]
print(arr)
        
