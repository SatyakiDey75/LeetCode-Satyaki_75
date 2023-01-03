class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=nums
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                l[i]='_'
        for i in range(len(l)):
            if l[i]=='_':
                l.remove(l[i])
                l.append('_')
        i,b=0,0
        try:
            while l[i]!='_':
                b+=1
                i+=1
        except:
            pass
        return b