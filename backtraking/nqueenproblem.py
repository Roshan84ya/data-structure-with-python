def queen(row,column, path , i , j):
    if i==row:
        for ii in range(5):
            for jj in range(5):
                if path[ii][jj]==1:
                    print("Q",end=" ")
                else:
                    print("-",end=" ")
            print()
        print()

    if i<0 or i>=row:
        return 

    for j in range(row):
        if placequeen(path,i,j):
            path[i][j]=1
            nextqueen=queen(row,column,path,i+1,j)
            if nextqueen:
                return True
            path[i][j]=0
    return False
            
        
        
        
    
        
def placequeen(path,i,j):
    if up(path,i,j) and  lupdiagnol(path,i,j) and rupdiagnol(path,i,j):
        return True
    
    




def up(path,i,j):
    if i<0 or i>=5 or j<0 or j>=5:
        return True
    if path[i][j]==1:
        return False
    if up(path,i-1,j):
        return True
    return False




def lupdiagnol(path,i,j):
    if i<0 or i>=5 or j<0 or j>=5:
        return True
    if path[i][j]==1:
        return False
    if lupdiagnol(path,i-1,j-1):
        return True
    return False
        

        
def rupdiagnol(path,i,j):
    if i<0 or i>=5 or j<0 or j>=5:
        return True
    if path[i][j]==1:
        return False
    if rupdiagnol(path,i-1,j+1):
        
        return True
    return False
    
    
path=[0]*5
for i in range(5):
    path[i]=[0]*5
queen(5,5,path,0,0)
