class Solution(object):
    def halvesAreAlike(self, s):
        l=['a', 'e', 'i', 'o', 'u']
        c1,c2=0,0
        s1,s2=s[:len(s)/2].lower(),s[len(s)/2:].lower()
        for i in l:
            if i in s1:
                c1+=s1.count(i)
            if i in s2:
                c2+=s2.count(i)
        return c1==c2