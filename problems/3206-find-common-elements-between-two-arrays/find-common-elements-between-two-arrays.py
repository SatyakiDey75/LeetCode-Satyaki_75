class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        min,max=list(set(nums1)),list(set(nums2))
        # if len(nums1)>len(nums2):
        #     min,max=list(set(nums2)),list(set(nums1))
        s,r=0,0
        # for i in min:
        #     if i in max:
        #         s+=nums1.count(i)
        #         r+=nums2.count(i)
        # return [s,r]
        for i in min:
            if i in max:
                s+=nums1.count(i)
                r+=nums2.count(i)
        return [s,r]
