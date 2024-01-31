class Solution(object):
    def kthFactor(self, n, k):
        l=[i for i in range(1,n//2+1) if n%i==0]
        l.append(n)
        return l[k-1] if k<=len(l) else -1