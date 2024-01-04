class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range (0,len(nums)):
            ls,rs=0,0
            for j in range(0,i):
                ls+=nums[j]
            for j in range(i+1,len(nums)):
                rs+=nums[j]
            l.append(max(ls,rs)-min(ls,rs))
        return l