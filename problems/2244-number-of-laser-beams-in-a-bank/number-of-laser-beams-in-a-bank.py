class Solution(object):
    def numberOfBeams(self, b):
        s=0
        for i in range (len(b)):
            if "1" in b[i]:
                for j in range (i+1,len(b)):
                    if "1" in b[j]:
                        s+=(b[i].count("1")*b[j].count("1"))
                        break
        return s