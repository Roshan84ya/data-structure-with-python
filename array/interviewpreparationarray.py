def arrayManipulation(n, queries):
    arr=[0]*n
    for i in queries:
        arr[i[0]-1]+=i[2]
        if i[1]<n:
            arr[i[1]]-=i[2]
    maxvalue=0
    ik=0
    for i in arr:
        ik+=i
        if ik>maxvalue:
            maxvalue=ik
    return maxvalue

n,m=map(int,input().split())
queries=[]
for i in range(m):
    queries.appen(list(map(int,input().split())))
print(arrayManipulation(n, queries))
