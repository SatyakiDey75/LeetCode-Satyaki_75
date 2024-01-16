class Solution(object):
    def isBoomerang(self, p):
        if p[1]==p[2] or p[2]==p[0] or p[0]==p[1]:
            return False
        c=p
        a=-(c[1][1]-c[0][1])
        b=(c[1][0]-c[0][0])
        c1=-a*c[0][0]-b*c[0][1]
        for i in range(2,len(c)):
            if (a*c[i][0]+b*c[i][1]+c1)!=0:
                return True
        return False
        