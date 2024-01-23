class Solution(object):
    def countSymmetricIntegers(self, l, h):
        c=0
        for i in range (l,h+1):
            s=str(i)
            if len(s)%2!=0:
                continue
            if len(s)==2:
                c+=1 if int(s[0])==int(s[1]) else 0
            else:
                c+=1 if int(s[0])+int(s[1])==int(s[2])+int(s[3]) else 0
        return c