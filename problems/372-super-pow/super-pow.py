class Solution(object):
    def superPow(self, a, b):
        s=0
        for i in b:
            s=s*10+i
        return pow(a,s,1337)
        