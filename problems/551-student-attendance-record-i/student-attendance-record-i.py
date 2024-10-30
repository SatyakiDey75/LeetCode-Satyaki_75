class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        for i in range (len(s)):
            if s[i] == 'L':
                try:
                    if s[i:i+3] == 'LLL':
                        return False 
                except:
                    continue
        return True