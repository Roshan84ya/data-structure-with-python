# the worst case complexity of this algo is N^2 but as this is randomized agorithm
#its time complextiy fluctuates betwee O(N2) to O(NlogN) and mostly it comes out
#to be O(NlogN)

def partition(arr,low,high):
    print(low,high)
    i=low-1
    pivot=arr[high]

    for j in range(low,high): #here i keep track of the element that is greater than the pivot element and we swap it with the smaller elemnet of the pivot
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]

    return (i+1)



def quickSort(arr,l,r):
    if l<r:
        pi=partition(arr,l,r)

        
        quickSort(arr,l,pi-1)
        
        quickSort(arr,pi+1,l)
        
        
        





arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(*arr)




