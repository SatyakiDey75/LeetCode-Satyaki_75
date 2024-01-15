class Solution(object):
    def checkStraightLine(self, c):
        if len(c)==2:
            return True
        else:
            a=-(c[1][1]-c[0][1])
            b=(c[1][0]-c[0][0])
            c1=-a*c[0][0]-b*c[0][1]
            for i in range(2,len(c)):
                if (a*c[i][0]+b*c[i][1]+c1)!=0:
                    return False
            return True