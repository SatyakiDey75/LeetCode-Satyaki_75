class Solution(object):
    def findDuplicate(self, nums):
        n=sorted(nums)
        return [n[i] for i in range (len(n)-1) if n[i]==n[i+1]][0]
        