class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans=[0]*len(temperatures)
        stk=[]
        for i,j in enumerate(temperatures):
            while stk and j>temperatures[stk[-1]]:
                i1=stk.pop()
                ans[i1]=i-i1
            stk.append(i)
        return ans
            