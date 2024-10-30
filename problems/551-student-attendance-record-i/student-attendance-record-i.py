class Solution:
    def checkRecord(self, s: str) -> bool:
        # if s.count('A') > 1:
        #     return False
        # for i in range (len(s)):
        #     if s[i] == 'L':
        #         try:
        #             if s[i:i+3] == 'LLL':
        #                 return False 
        #         except:
        #             continue
        # return True

        # if s.count('A') > 1:
        #     return False
        # l = len(s)
        # if l <= 2:
        #     return True
        # for i in range (len(s) - 2):
        #     if s[i] == s[i+1] == s[i+2] == 'L':
        #         return False
        # return True

        A, L, i = 0, 0, 0
        while i < len(s):
            if s[i] == "A": 
                A += 1
                if A >= 2:
                    return False
            if s[i] == "L":
                L += 1
                if L >= 3:
                    return False
            else:
                L = 0
            i += 1
        return True