class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        x=2**n
        l=[]
        for i in range (0,x):
            l.append(i^(i>>1))
        return l