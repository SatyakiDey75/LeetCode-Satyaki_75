class Solution(object):
    def merge(self, inte):
        l=[]
        for i in sorted(inte):
            if not l or l[-1][1]<i[0]:
                l.append(i)
            else:
                l[-1][1]=max(l[-1][1],i[1])
        return l
            