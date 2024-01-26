class Solution(object):
    def trimMean(self, arr):
        rm=0.05*len(arr)
        arr.sort()
        s,n=0,0.0
        for i in range(int(rm),int(len(arr)-rm)):
            s+=arr[i]
            n+=1
        return s/n
        