class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S=["0"]
        for i in range (1,n+1):
            a,c="",""
            b=S[i-1]
            for i in (S[i-1]):
                if i=="0":
                    i='1'
                    c+=i
                else:
                    i="0"
                    c+=i
            a=b+'1'+c[::-1]
            S.append(a)
        return S[n-1][k-1]
