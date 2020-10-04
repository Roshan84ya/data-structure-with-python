#recursive approch
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row=len(grid)
        column=len(grid[0])
        return self.findpath(0,0,grid,row,column)
    
    def findpath(self,i,j,arr,row,column):
        if i<0 or i>=row or j<0 or j>=column:
            return 10000000000
        if i==(row-1) and (j==column-1):
            return arr[i][j]
        
        d=arr[i][j]+self.findpath(i+1,j,arr,row,column)
        r=arr[i][j]+self.findpath(i,j+1,arr,row,column)
        return min(d,r)
       

#memoization
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row=len(grid)
        column=len(grid[0])
        dp=[-1]*(row)
        for i in range(row):
            dp[i]=[-1]*column
        return self.findpath(0,0,grid,row,column,dp)
    
    def findpath(self,i,j,arr,row,column,dp):
        if i<0 or i>=row or j<0 or j>=column:
            return 10000000000
        if i==(row-1) and (j==column-1):
            return arr[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        
        d=arr[i][j]+self.findpath(i+1,j,arr,row,column,dp)
        r=arr[i][j]+self.findpath(i,j+1,arr,row,column,dp)
        dp[i][j]=min(d,r)
        return dp[i][j]
       
        
    
        
