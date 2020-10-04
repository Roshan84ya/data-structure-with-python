#here we are focussing on an element should be palced on its correct position and swap all the element next to its corrext posititon till we got the the previous one is smaller than the next one



arr=[4,3,2,1,8,9]
sum=0
for i in range(1,len(arr)):
    c=0
    #here we assing a next value to the key
    key=arr[i]
    #here we took th3 index-1 of key value
    j=i-1
     #here we compare the ondex must be greater than 0or equal and the next value is smaller than the previous one
    while j>=0 and key<arr[j]:
        #if our condition satisfies then we swap the two elements till our condition fails i.e the next one is smaller than the previous one or it should be like the next one must be the greater than its previous one.
        arr[j],arr[j+1]=arr[j+1],arr[j]
        c+=1
        
        j-=1
    sum+=c
    print(c)
print(arr)
