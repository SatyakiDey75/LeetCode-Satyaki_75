class Solution(object):
    def xorOperation(self, n, start):
        s=0
        for i in range (n):
            s^=start+(2*i)
        return s
        