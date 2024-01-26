class Solution(object):
    def deleteGreatestValue(self, grid):
        m,s=len(grid),0
        while grid[0]!=[]:
            l=[]
            for i in range(m):
                l.append(max(grid[i]))
                grid[i].remove(max(grid[i]))
            s+=max(l)
        return s