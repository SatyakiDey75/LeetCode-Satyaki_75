class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        for i, num in enumerate(nums):
            hmap[num] = i
        for i, num in enumerate(nums):
            sol = target - num
            if sol in hmap and hmap[sol] != i:
                return i, hmap[sol]