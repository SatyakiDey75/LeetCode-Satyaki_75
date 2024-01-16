class Solution(object):
    def halvesAreAlike(self, s):
        l='aeiou'
        s1,s2=s[:len(s)/2].lower(),s[len(s)/2:].lower()
        return sum(s1.count(i) for i in l)==sum(s2.count(i) for i in l)