class Solution(object):
    def thirdMax(self, nums):
        l=list(sorted(set(nums)))
        print(l)
        if len(l)<3:
            return l[-1]
        return l[-3]