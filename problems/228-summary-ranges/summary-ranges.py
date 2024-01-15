class Solution(object):
    def summaryRanges(self, nums):
        l=[]
        i=0
        while i<len(nums):
            j=i
            while j+1<len(nums) and nums[j+1]-nums[j]==1:
                j+=1
            if i==j:
                l.append(str(nums[j])) 
            else:
                l.append(str(nums[i])+"->"+str(nums[j]))
            i=j+1
        return l