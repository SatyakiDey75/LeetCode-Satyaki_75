class Solution(object):
    def arrangeWords(self, text):
        l=text.split(" ")
        k,v,l1=[],[],[]
        for i in l:
            k.append(i)
            v.append(len(i))
        if len(set(v))==1:
            return text
        v1=sorted(v)
        for i in range(len(l)):
            l=v.index(v1[i])
            l1.append(k[l])
            v[l]=-8

        return " ".join(l1).capitalize()
