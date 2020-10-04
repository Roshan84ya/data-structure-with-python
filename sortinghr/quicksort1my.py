def quicksort(arr,l,h):
    if l<h:
        
        pi=partition(arr,l,h)




        
        quicksort(arr,l,pi-1)
        
        quicksort(arr,pi+1,h)
    return arr

def partition(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
            
    return i+1

arr=[10,30,80,90,40,50,70]
l=0
h=len(arr)-1

result=quicksort(arr,l,h)
print(result)

