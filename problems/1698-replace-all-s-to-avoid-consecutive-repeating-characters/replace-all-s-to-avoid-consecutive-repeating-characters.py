class Solution(object):
    def modifyString(self, s):
        s1="abcdefghijklmnopqrstuvwxyz"
        l=list(s)
        if s=="?":
            return 'f'
        for i in range (len(s)):
            t=s1
            if l[i]=='?':
                if i==0:
                    l[i]=t.replace(l[i+1],"")[0]
                elif i==len(s)-1:
                    l[i]=t.replace(l[i-1],"")[0]
                else:
                    l[i]=t.replace(l[i-1],"").replace(l[i+1],"")[0]
        return "".join(l)
        