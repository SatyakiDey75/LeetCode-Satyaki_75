class Solution(object):
    def sortArrayByParity(self, nums):
        n1,i=[],0
        while i<len(nums):
            if nums[i]%2!=0:
                n1.append(nums[i])
                nums.remove(nums[i])
                i-=1
            i+=1
        return nums+n1