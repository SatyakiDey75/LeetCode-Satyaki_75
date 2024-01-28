class Solution(object):
    def removeStars(self, s):
        l=[]
        for i in s:
            if i=='*':
                l.pop()
            else:
                l.append(i)
        return "".join(l)