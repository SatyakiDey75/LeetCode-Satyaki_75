class Solution(object):
    def frequencySort(self, nums):
        cnt=Counter(nums)
        return sorted(nums,key=lambda x:(cnt[x],-x))
        