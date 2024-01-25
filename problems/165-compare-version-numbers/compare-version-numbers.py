class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        r1=v1.split('.')
        r2=v2.split('.')
        if len(r1)>len(r2):
            for i in range (len(r1)-len(r2)):
                r2.append('0')
        
        elif len(r1)<len(r2):
            for i in range (len(r2)-len(r1)):
                r1.append('0')
        for i in range (len(r1)):
            if int(r1[i])>int(r2[i]):
                return 1
            if int(r1[i])<int(r2[i]):
                return -1
        return 0
        