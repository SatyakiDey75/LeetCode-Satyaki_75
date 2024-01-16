class Solution(object):
    def isBoomerang(self, p):
        if p[1]==p[2] or p[2]==p[0] or p[0]==p[1]:
            return False
        x1,y1=p[0][0],p[0][1]
        x2,y2=p[1][0],p[1][1]
        x3,y3=p[2][0],p[2][1]
        return (y3-y2)*(x2-x1)!=(y2-y1)*(x3-x2)