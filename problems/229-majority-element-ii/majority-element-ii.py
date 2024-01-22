class Solution(object):
    def majorityElement(self, nums):
        l,s=[],len(nums)//3
        for i in set(nums):
            if nums.count(i)>s:
                l.append(i)
        return l        