class Solution(object):
    def sortArrayByParity(self, nums):
        n1,n2=[],[]
        for i in nums:
            if i%2==0:
                n1.append(i)
                continue
            n2.append(i)
        return n1+n2