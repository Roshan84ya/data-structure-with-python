#selcection sort is based on thr idea of finfing the minimum element and putting it on the correct position
#here im asssuming the current index is the index of the minimum element and the i go and iterate fro the index value i+1 to the end and if i find some element that is smaller than the current
#element the we swap it with that element

arr=[7,5,4,2]
for i in range(len(arr)):
    minimum=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[minimum]:
            minimum=j
    arr[i],arr[minimum]=arr[minimum],arr[i]
print(*arr)
