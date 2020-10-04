def insertionSort(arr):
    swap=0
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)):
        flag=0
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
                flag=1
        arr[j + 1] = key
        if flag:
            swap+=1
    return swap
  
  
# Driver code to test above 
n=int(input())
k=list(map(int,input().split()))
print(insertionSort(k))
