class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split(" ")
        s1=''
        for i in range(len(l)-1,0,-1):
            if l[i]!='':
                s1=s1+l[i]+" "
        if l[0]!='':
            s1+=l[0]
        else:
            s1=s1[:-1]
        return s1