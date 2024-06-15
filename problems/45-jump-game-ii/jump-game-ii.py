class Solution(object):
    def jump(self, n):
        i,e=0,0
        c,f=0,0
        if len(n)==1:
            return 0
        while i<len(n):
            f=max(f,i+n[i])
            if f>=len(n)-1:
                return c+1
            if i==e:
                c+=1
                e=f
            i+=1
        return c