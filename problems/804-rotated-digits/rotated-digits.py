def rot(n):
    n1=list(str(n))
    d={'0':'0','1':'1','2':'5','5':'2','6':'9','8':'8','9':'6'}
    for i in range (len(n1)):
        if n1[i] not in d:
            return n
        n1[i]=d[n1[i]]
    s=0
    for i in n1:
        s=s*10+int(i)
    return s

class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(1 for i in range (1,n+1) if i!=rot(i))
