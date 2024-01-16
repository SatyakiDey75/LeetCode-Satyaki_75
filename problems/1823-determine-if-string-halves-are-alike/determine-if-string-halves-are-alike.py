class Solution(object):
    def halvesAreAlike(self, s):
        l=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c1,c2=0,0
        s1,s2=s[:len(s)/2],s[len(s)/2:]
        for i in l:
            if i in s1:
                c1+=s1.count(i)
            if i in s2:
                c2+=s2.count(i)
        return c1==c2