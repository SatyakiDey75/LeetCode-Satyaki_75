class Solution(object):
    def findSpecialInteger(self, arr):
        a=[i for i in arr if arr.count(i)>len(arr)/4]
        return a[0]
        