class Solution(object):
    def lexicalOrder(self, n):
        l=sorted([str(i) for i in range (1,n+1)])
        l=[int(i) for i in l]
        return l