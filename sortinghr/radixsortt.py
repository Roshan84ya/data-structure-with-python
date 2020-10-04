def radixsort(arr,ij):
    if ij<n:
        d={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        for i in arr:
            q=i
            if ij>1:
                q=i//(10**(ij-1))
            t=q%10

            d[t].append(i)

        k=[]
        for i in d:
            k=k+d[i]
        return radixsort(arr,ij+1)
    else:
        return arr


arr=[10,21,17,34,44,11,654,123]
n=len(str(max(arr)))

print(radixsort(arr,1))
