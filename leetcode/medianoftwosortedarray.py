nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))

l1=len(nums1)
l2=len(nums2)

i=0
j=0
arr=[]
st=(l1+l2)//2
s=0
a,b=0,0
while len(arr)<=st and i<l1 and j<l2:
    if nums1[i]<nums2[j]:
        
        i+=1
    else:
        arr.append(nums2[j])
        j+=1
while len(arr)<=st and i<l1:
    arr.append(nums1[i])
    i+=1

    

while len(arr)<=st and j<l2:
   arr.append(nums2[j])
   j+=1
if (l1+l2)%2==0:
    print((arr[-1]+arr[-2])/2)
else:
    print(arr[-1])
