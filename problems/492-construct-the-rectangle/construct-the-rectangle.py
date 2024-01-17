class Solution(object):
    def constructRectangle(self, area):
        j=int(sqrt(area))
        while area%j!=0:
            j-=1
        return [area/j,j]
        