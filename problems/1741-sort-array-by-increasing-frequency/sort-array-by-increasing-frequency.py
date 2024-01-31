class Solution(object):
    def frequencySort(self, nums):
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return sorted(nums,key=lambda x:(d[x],-x))
        