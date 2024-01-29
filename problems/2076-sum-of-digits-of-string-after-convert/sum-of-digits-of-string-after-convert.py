def sod(i):
    s=0
    while i>0:
        s+=i%10
        i//=10
    return s

class Solution(object):
    def getLucky(self, s, k):
        a=""
        for i in s:
            a+=str(ord(i)-96)
        s=int(a)
        print(a)
        for i in range (k):
            s=sod(s)
        return s