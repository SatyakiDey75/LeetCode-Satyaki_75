class Solution(object):
    def superPow(self, a, b):
        s=1
        for i in b[::-1]:
            s=(s*pow(a,i,1337))%1337
            a=pow(a,10,1337)
        return s
        