class Solution(object):
    def countTestedDevices(self, bp):
        c=0
        for i in range (len(bp)):
            if bp[i]>0:
                c+=1
                bp[i+1:]=[max(0,bp[j]-1) for j in range (i+1,len(bp))]
        return c