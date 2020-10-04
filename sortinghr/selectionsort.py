def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            arr[i],arr[temp[i+1]] = i+1,arr[i]
            temp[arr[temp[i+1]]] = temp[i+1]
    return swaps

arr=[4,3,1,2]
print(minimumSwaps(arr))

