class Solution(object):
    def trimMean(self, arr):
        rm=0.05*len(arr)
        arr.sort()
        s=sum(arr[int(rm):int(-1*rm)])
        return s/(len(arr)-(2*rm))
        