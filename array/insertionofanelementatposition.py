#insertion_of_an_element_int_the_Array

arr=[1,2,3,4,5]
n=int(input("Enter the element to be inserted: "))
pos=int(input("Enter the posititon of insetion: "))
arr.append(0)
for i in range(len(arr)-1,pos-1,-1):
    arr[i]=arr[i-1]


arr[pos-1]=n
print(arr)
    
