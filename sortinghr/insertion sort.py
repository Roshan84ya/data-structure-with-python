k=[1,4,3,5,6,2]

for i in range(len(k)-1):
    
    if k[i]>k[i+1]:
        temp=k[i+1]  #temp=3 and j=index of 5
        j=i
        while temp<k[j] and j>=0:
            k[j+1]=k[j]
            
            j-=1
        k[j+1]=temp
    print(k)
        

            
            
        
