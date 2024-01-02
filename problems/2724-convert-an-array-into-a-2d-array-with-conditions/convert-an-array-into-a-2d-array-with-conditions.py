def mat(nums):
        l,l1=[],[]
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l1.append(i)
        return l,l1

class Solution(object):
    
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[]
        c=mat(nums)
        l.append(c[0])
        while c[1]!=[]:
            c=mat(c[1])
            l.append(c[0])
        return l

        