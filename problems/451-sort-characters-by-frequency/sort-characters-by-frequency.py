class Solution(object):
    def frequencySort(self, s):
        all_freq={}
        res=""
        for i in s:
            if i in all_freq:
                all_freq[i]+=1
            else:
                all_freq[i]=1
        rl = sorted(all_freq.items(),key=lambda x:x[1],reverse=True)
        for i in rl:
            res+=(i[0]*i[1])
        return res