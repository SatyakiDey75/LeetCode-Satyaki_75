class Solution(object):
    def capitalizeTitle(self, t):
        l=t.split()
        for i in range(len(l)):
            if len(l[i])>2:
                l[i]=l[i].capitalize()
            else:
                l[i]=l[i].lower()
        return ' '.join(l)