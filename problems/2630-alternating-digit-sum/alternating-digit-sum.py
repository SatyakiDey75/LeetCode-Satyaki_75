class Solution(object):
    def alternateDigitSum(self, num):
        n,s=str(num),0
        for i in range(len(n)):
            if i%2==0:
                s+=int(n[i])
            else:
                s-=int(n[i])
        return s