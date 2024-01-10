class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        s1,s2=set(nums1),set(nums2)
        return [sum(i in s2 for i in nums1), sum(i in s1 for i in nums2)]
