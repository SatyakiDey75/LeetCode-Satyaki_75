class Solution(object):
    def maxFrequencyElements(self, nums):
        d={}
        for i in nums:
            if d.get(i):
                d[i]+=1
            else:
                d[i]=1
        max=0
        co=0
        for i,j in d.items():
            if max<j:
                max=j
                co=j
            elif max==j:
                co+=j
        return co