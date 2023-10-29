def bd(b):
    d,i=0,0
    while b!=0:
        d+=(b%10)*(2**i)
        b=b//10
        i+=1
    return d

def db(n):
    d=0
    i=0
    while n!=0:
        d+=(n%2)*(10**i)
        i+=1
        n=n//2
    return d


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1=int(a)
        b1=int(b)
        c=bd(a1)+bd(b1)
        return str(db(c))