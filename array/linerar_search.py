#linear_searching_for unsorted array
a=[20,5,7,25]
s=int(input("Enter the element to be searched: "))
for i in range(len(a)):
    if s==a[i]:
        print("Element found at the {} place".format(i+1))
        break
