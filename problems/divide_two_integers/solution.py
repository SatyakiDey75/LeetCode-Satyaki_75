class Solution:
    def divide(self, d: int, n: int) -> int:
        b=0
        c=0
        if abs(d)<abs(n):
            return 0
        if n>0:
            if d<0:
                n=-n
                c=d//n
                b=-c
            else:
                b= d//n
        else:
            if d>0:
                n=-n
                c=d//n
                b=-c
            else:
                b= d//n
        if b>(2**31)-1:
            return (2**31)-1
        elif b<-(2**31):
            return -(2**31)
        else:
            return b