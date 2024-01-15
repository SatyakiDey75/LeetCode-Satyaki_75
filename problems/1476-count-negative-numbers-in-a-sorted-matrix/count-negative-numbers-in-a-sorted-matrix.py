class Solution(object):
    def countNegatives(self, grid):
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]<0):
                    c+=1
        return c 
        