class Solution(object):
    def findLonely(self, nums):
        l=[]
        d=Counter(nums)
        for i,j in d.items():
            if(d[i-1]==0 and d[i+1]==0 and j==1):
                l.append(i)
        return l
        