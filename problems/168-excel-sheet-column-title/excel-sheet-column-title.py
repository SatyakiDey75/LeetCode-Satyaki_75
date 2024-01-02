class Solution(object):
    def convertToTitle(self, c):
        s=''
        while c>0:
            if c%26>0: 
                s+=chr(64+(c%26))
                c//=26
            else: 
                s+='Z'
                c=(c//26)-1
        return s[::-1]