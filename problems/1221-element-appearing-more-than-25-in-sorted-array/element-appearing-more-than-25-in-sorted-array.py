class Solution(object):
    def findSpecialInteger(self, arr):
        q=len(arr)//4
        for i in range(len(arr)-q):
            if arr[i]==arr[i+q]:
                return arr[i]
                