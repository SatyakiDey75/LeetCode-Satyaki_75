class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        kMod=1_000_000_007
        n=len(arr)
        ans=0
        pM=[-1]*n
        nM=[n]*n
        stk=[]
        for i,a in enumerate(arr):
            while stk and arr[stk[-1]]>a:
                index=stk.pop()
                nM[index]=i
            if stk:
                pM[i]=stk[-1]
            stk.append(i)
        for i, a in enumerate(arr):
            ans+=a*(i-pM[i])*(nM[i]-i)
            ans%=kMod
        return ans