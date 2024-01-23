class Solution(object):
    def findDuplicates(self, nums):
        s,a={},[]
        for i in nums:
            if i in s:
                s[i]+=1
                a.append(i)
            else:
                s[i]=1
        return a