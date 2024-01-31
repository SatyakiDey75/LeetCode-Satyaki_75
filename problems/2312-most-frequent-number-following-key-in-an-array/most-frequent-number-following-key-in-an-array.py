class Solution(object):
    def mostFrequent(self, nums, key):
        count=collections.Counter()
        for i,j in zip(nums,nums[1:]):
            if i==key:
                count[j]+=1
        return max(count,key=lambda k:count[k])
            