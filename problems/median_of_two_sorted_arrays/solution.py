class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        l.sort()
        i=int((len(l)-1)/2)
        j=int((len(l)/2))
        if len(l)%2!=0:
            return (l[i])
        else:
            return ((l[j])+(l[j-1]))/2
