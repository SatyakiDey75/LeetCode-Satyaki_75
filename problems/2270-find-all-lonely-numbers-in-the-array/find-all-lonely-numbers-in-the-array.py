class Solution(object):
    def findLonely(self, nums):
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in nums:
            if d[i]==1 and i-1 not in d and i+1 not in d:
                l.append(i)
        return l
        