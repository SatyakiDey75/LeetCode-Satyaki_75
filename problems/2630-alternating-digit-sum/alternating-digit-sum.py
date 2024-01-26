class Solution(object):
    def alternateDigitSum(self, n):
        # return sum(int(j) if i%2==0 else -int(j) for i,j in enumerate(str(n)))
        s=0
        for i,j in enumerate(str(n)):
            if i%2==0:
                s+=int(j)
            else:
                s-=int(j)
        return s