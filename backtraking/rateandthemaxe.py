def findpath(arr,path, row , column , i, j):
    #if i,j goes out of the index
    if i<0 or i>=row or j<0 or j>=column:
        return 

    if i==(row-1) and j==(column-1):
        path[i][j]=1
        print(path)
        
    if arr[i][j]==0 or path[i][j]==1:
        return 

    path[i][j]=1

    #right
    findpath(arr,path,row,column,i,j+1)
        

    
    findpath(arr,path,row,column,i,j-1)
        

    #up
    findpath(arr,path,row,column, i-1,j)
        

    #down
    findpath(arr,path,row,column,i+1,j)
        
    
    
    
    

def find(arr):
    row=len(arr)
    column=len(arr[0])
    path=[0]*row
    for i in range(row):
        path[i]=[0]*column

    findpath(arr,path,row,column,i=0,j=0)
    
arr=[
    [1,0,0],
    [1,1,1],
    [0,1,1],
    ]
find(arr)
