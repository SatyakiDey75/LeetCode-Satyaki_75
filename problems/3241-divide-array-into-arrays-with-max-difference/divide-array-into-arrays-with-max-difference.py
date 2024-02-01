class Solution(object):
    def divideArray(self, nums, k):
        l=[]
        nums.sort()
        for i in range(2,len(nums),3):
            if nums[i]-nums[i-2]>k:
                return []
            l.append([nums[i-2],nums[i-1],nums[i]])
        return l
            