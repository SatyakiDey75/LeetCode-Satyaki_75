class Solution(object):
    def squareIsWhite(self, c):
        a={'a','c','e','g'}
        b={'b','d','f','h'}
        if c[0] in a:
            if int(c[1])%2==0:
                return True
            return False
        else:
            if int(c[1])%2==0:
                return False
            return True