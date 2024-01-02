def let(i):
    s='Z'
    if i%26>0:
        s=chr(64+(i%26))
    return s

class Solution(object):
    def convertToTitle(self, c):
        s=''
        while c>0:
            s+=let(c)
            if c%26==0: c=(c//26)-1
            else: c//=26
        return s[::-1]
