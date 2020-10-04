def radixsort(a,ij):
    
    if ij<=n:
        #here we have table in which we store data
        dic={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

        
        for i in a:
            q=i
            if ij>1:
                q=i//(10**(ij-1))
                
            t=q%10
            
            
            dic[t].append(i)
        
            
        k=[]
        #taking element from left to right and from top to bottom
        for i in dic:
            k=k+dic[i]
        ij+=1
        
        
        return radixsort(k,ij)
    else:
        return a
    
    
    
a=list(map(int,input().split()))
n=len(str(max(a)))
result=radixsort(a,1)
print(result)



