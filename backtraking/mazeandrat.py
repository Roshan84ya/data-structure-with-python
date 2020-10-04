"""
this problem is rat in the  maze problem that is based on the concept of the backtracking
i.e rat is at the position of 00 and he need to move to the bottom right corner to reach at the home and he can move upward downward anf left and right

"""

def findpath(maze,n,x,y,path):
    #the first condition it will check whether the point is in the boundry or not and  it will return false if our point is found out of the bond
    if x<0 or x>=n or y<0 or y>=n: #out of the boundry
        return False

    #here is our base condition i.e if we reach at the home then we return the true
    if x==n-1 and y==n-1:
        path[x][y]=1
        return True

    #here we see if we move on the x,y or not as the maze=0 will show that there is no path and path =1 will show that we were already gone there
    if maze[x][y]==0 or path[x][y]==1:
        return False
    #here we set the path i.e we are taking that path
    path[x][y]=1
    #right
    if findpath(maze,n,x,y+1,path):
        path[x][y]=0
        return True
    #left
    if findpath(maze,n,x,y-1,path):
        path[x][y]=0
        return True
    #top
    if findpath(maze,n,x-1,y,path):
        path[x][y]=0
        return True
    #down
    if findpath(maze,n,x+1,y,path):
        path[x][y]=0
        return True
    path[x][y]=0
    return False


def findpa(maze,n):
    path=[0]*n #path will track whether we are gone through that node of not 
    for i in range(n):
        path[i]=[0]*3
    return findpath(maze,n,0,0,path)
##############################################################################################################################################################
                                                """ MAIN """
#here we will take n input the size of the array
n=int(input())
arr=[[1,1,0],
     [1,1,0],
     [0,1,1]
     ]
print(findpa(arr,n=3))
