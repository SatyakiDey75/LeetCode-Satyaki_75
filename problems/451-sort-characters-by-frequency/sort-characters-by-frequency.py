class Solution(object):
    def frequencySort(self, s):
        af={}
        res=""
        for i in s:
            if i in af:
                af[i]+=1
            else:
                af[i]=1
        rl = sorted(af.items(),key=lambda x:x[1],reverse=True)
        for i in rl:
            res+=(i[0]*i[1])
        return res