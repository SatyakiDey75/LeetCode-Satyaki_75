class Solution(object):
    def checkOnesSegment(self, s):
        if s.count('1')==1:
            return True
        for i in range (len(s)-1):
            if s[i]=='0' and s[i+1]=='1':
                return False
        return True
        