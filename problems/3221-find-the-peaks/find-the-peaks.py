class Solution(object):
    def findPeaks(self, m):
        i=1
        l=[]
        while i<len(m)-1:
            if m[i]>m[i-1] and m[i]>m[i+1]:
                l.append(i)
                i+=1
            i+=1
        return l