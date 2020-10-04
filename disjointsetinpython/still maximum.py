def root(a):
    while arr[a]!=a:
        arr[a]=arr[arr[a]]
        a=arr[a]
    return a
def uni(a,b,realmax):
    roota=root(a)
    rootb=root(b)
    one_node=arrayminmax[roota]
    second_node=arrayminmax[rootb]
    arrayminmax[roota]=[min(one_node[0],second_node[0]),max(one_node[1],second_node[1])]
    arrayminmax[rootb]=[min(one_node[0],second_node[0]),max(one_node[1],second_node[1])]
    if size[roota]<size[rootb]:
        arr[roota]=rootb
        size[rootb]+=size[roota]

        size[roota]=0
    else:
        
        arr[rootb]=roota
        size[roota]+=size[rootb]
        size[rootb]=0
    return realmax,max(realmax,abs(arrayminmax[roota][0]-arrayminmax[roota][1]))
    



n=int(input())
#edgelist
edgelist=list()
arr=[i for i in range(n)]
size=[1]*(n)
for _ in range(n-1):
    a,b=map(int,input().split())
    edgelist.append([a-1,b-1])
#specialvalue

speacialvalue=[int(i) for i in input().split()]

#operation_list
operationlist=list()
for _ in range(n-1):
    operationlist.append(int(input()))

result=[]
arrayminmax=[[i,i] for i in speacialvalue]

realmax=0
while len(operationlist):
    k=operationlist.pop()
    a,b=edgelist[k-1]
    
    ans,realmax=uni(a,b,realmax)
    result.append(ans)
    
for i in result[::-1]:
    print(i)
    
        





