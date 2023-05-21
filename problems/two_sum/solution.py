class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p=[]
        for i in range (0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    p.append(i)
                    p.append(j)
                    break
        return p[0:2]