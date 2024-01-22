def se(t,d):
    ke=sorted(list(d.keys()))
    for i in ke:
        if d[i]==t:
            return i

class Solution(object):
    def mostFrequentEven(self, nums):
        d={}
        for i in nums:
            if i%2==0:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        if len(d)==0:
            return -1
        val=sorted(list(d.values()))
        return se(val[-1],d)