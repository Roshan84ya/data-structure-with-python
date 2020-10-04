# the worst case complexity of this algo is N^2 but as this is randomized agorithm
#its time complextiy fluctuates betwee O(N2) to O(NlogN) and mostly it comes out
#to be O(NlogN)

def partition(arr,low,high): 
    i = ( low-1 )         
    pivot = arr[high]    
  
    for j in range(low , high):  
        if   arr[j] < pivot: 
          
            
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,low,high): 
    if low < high: 
 
        pi = partition(arr,low,high)  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)           
    





kl=[10,30,80,90,40,50,70]
quickSort(kl,0,len(kl)-1)
print(kl)

