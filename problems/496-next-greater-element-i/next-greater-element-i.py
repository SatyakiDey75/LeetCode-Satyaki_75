class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        r=[]
        for i in nums1:
            f=0
            j=nums2.index(i)
            for k in range(j+1,len(nums2)):
                if nums2[k]>nums2[j]:
                    r.append(nums2[k])
                    f=1
                    break
            if f==0:
                r.append(-1) 
        return r