#reverse ofa n array

arr=[1,2,3,4,5,6]
i=0
h=len(arr)-1
while i<h:
    
    arr[i],arr[h]=arr[h],arr[i]
    i+=1
    h-=1
print(arr)
