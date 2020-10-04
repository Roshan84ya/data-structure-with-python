#The array of the size n is firstly divided into logN part then all the parts and
#merging all the single list takes O(N) time, the worst case run time of this
#algorithm is O(NlogN)


def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        a=arr[:mid]
        b=arr[mid:]
        mergeSort(a)
        mergeSort(b)

        
        i=j=k=0
        
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                arr[k]=a[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
            k+=1

         
        while i<len(a):
            arr[k]=a[i]
            i+=1
            k+=1
        
        
        while  j<len(b):
            arr[k]=b[j]
            k+=1
            j+=1
        



a = [12, 11, 13, 5, 6, 7] 
print("Given array is") 
print(*a) 
  
mergeSort(a) 
  
 
print("Sorted array is : ") 
print(*a) 
