class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        min,max=(list(set(nums1)),list(set(nums2))) if len(nums1)<len(nums2) else (list(set(nums2)),list(set(nums1)))
        l=[0]*2
        for i in min:
            if i in max:
                l[0]+=nums1.count(i)
                l[1]+=nums2.count(i)
        return l
