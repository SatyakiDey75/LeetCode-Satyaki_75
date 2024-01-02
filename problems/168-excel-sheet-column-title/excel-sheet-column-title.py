class Solution(object):
    def convertToTitle(self, c):
        s=''
        while c>0:
            if c%26>0: s+=chr(64+(c%26))
            else: s+='Z'
            if c%26==0: c=(c//26)-1
            else: c//=26
        return s[::-1]
