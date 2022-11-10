class Solution:
    def reverse(self, x: int) -> int:
        s=""
        if x>=-2147483648 and x<=2147483647:
            a=str(x)
            if len(a)==1:
                return a
            while a[-1]=="0" and len(a)>1:
                a=a[0:-1]
            if x<0:
                s= ("-"+a[:0:-1])
            else:
                s= (a[::-1])
            if int(s)>=-2147483648 and int(s)<=2147483647:
                return s
            else:
                return 0

        else:
            return 0