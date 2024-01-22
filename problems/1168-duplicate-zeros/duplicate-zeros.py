class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        while i<len(arr):
            if arr[i]==0:
                arr.insert(i,0)
                i+=2
                arr.pop()
            else:
                i+=1