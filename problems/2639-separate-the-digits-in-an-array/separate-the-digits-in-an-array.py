class Solution(object):
    def separateDigits(self, nums):
        # optimised:
        s=[]
        for i in nums:
            t=[]
            while i>0:
                t.append(i%10)
                i//=10
            s.extend(t[::-1])
        return s

        # brute force:
        # l=[str(i) for i in nums]
        # s=[]
        # for i in l:
        #     s+=[int(j) for j in list(i)]
        # return s
        