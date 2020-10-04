a=[5,4,3,2,1]

#here we compare the array element to the next element and if the next element is smaller then we swap
#the both element
#here is the optimized version of the bubble sort as if we dont found such element
#that is greter to next means our array is already sorted so we break there and hence we found the sorted array

#note and each time we place the biggest element at the end so for every iteration we don't need
# to iterate over the last element

for i in range(len(a)):
    flag=1
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            flag=0
    if flag:
        break
print(a)
