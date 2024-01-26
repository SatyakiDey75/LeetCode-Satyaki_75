class Solution(object):
    def deleteGreatestValue(self, grid):
        for i in grid:
            i.sort(reverse=True)
        s=0
        for i in zip(*grid):
            s+=max(i)
        return s

        # m,s=len(grid),0
        # while grid[0]!=[]:
        #     l=[]
        #     for i in range(m):
        #         l.append(max(grid[i]))
        #         grid[i].remove(max(grid[i]))
        #     s+=max(l)
        # return s