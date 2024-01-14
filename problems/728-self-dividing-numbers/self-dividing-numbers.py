def sdn(n):
    b=n
    while b>0:
        if b%10==0 or n%(b%10)!=0:
            return 0
        b//=10
    return 1

class Solution(object):
    def selfDividingNumbers(self, l, r):
        li=[]
        for i in range (l,r+1):
            if sdn(i)==1:
                li.append(i)
        return li