class Solution:
    def longestCommonPrefix(self, l: List[str]) -> str:
        if len(l)==1:
            return l[0]
        else:
            l.sort(key=len)
            s=l.pop(0)
            l1=[]
            for i in l:
                    p=""
                    for j in range (len(s)):
                            if i[j]==s[j]:
                                    p=p+s[j]
                            else:
                                if p!="":
                                        break
                    if p!="":
                        if p[0]!=i[0]:
                                p=p.replace(p[0],'')
                    l1.append(p)
            a=""
            if l1!=[]:
                l1.sort(key=len)
                a=l1[0]
            return (a)
                        
