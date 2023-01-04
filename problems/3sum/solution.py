class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        l=[]
        l2=[]
        ns=sorted(n)
        for i in range(len(n)-2):    
            st=i+1
            en=len(n)-1
            while st<en:
                rs=ns[i]+ns[st]+ns[en]
                if rs==0:
                    l.append((ns[i],ns[st],ns[en]))
                    st+=1
                    en-=1
                elif rs<0:
                    st+=1
                else:
                    en-=1
        return [list(i) for i in set(l)]