class Solution(object):
    def strStr(self, h, n):
        hl,nl=len(h),len(n)
        for i in range (hl):
            j=0
            for k in range (i,hl):
                if h[k]==n[j]:
                    j+=1
                else:
                    break
                if j==nl:
                    return i
        return -1
        