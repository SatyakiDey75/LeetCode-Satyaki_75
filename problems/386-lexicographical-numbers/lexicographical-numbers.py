class Solution(object):
    def lexicalOrder(self, n):
        l=[i for i in range(1,n+1)]
        l.sort(key=lambda x:str(x))
        return l