class Solution(object):
    def majorityElement(self, nums):
        l=[]
        for i in nums:
            if nums.count(i)>len(nums)/3 and i not in l:
                l.append(i)
        return l        