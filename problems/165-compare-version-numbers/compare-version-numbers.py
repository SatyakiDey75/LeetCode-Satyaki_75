class Solution(object):
    def compareVersion(self, v1, v2):
        r1=[int(i) for i in v1.split('.')]
        r2=[int(i) for i in v2.split('.')]
        ml=max(len(r1),len(r2))
        r1.extend([0]*(ml-len(r1)))
        r2.extend([0]*(ml-len(r2)))
        for i in range (ml):
            if r1[i]>r2[i]:
                return 1
            if r1[i]<r2[i]:
                return -1
        return 0
        