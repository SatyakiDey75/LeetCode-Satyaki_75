class Solution(object):
    def separateDigits(self, nums):
        l=[str(i) for i in nums]
        s=[]
        for i in l:
            s+=[int(j) for j in list(i)]
        return s
        