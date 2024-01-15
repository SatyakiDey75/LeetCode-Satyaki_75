class Solution(object):
    def checkIfExist(self, arr):
        if arr.count(0)>=2:
            return True
        for i in arr:
            if i*2 in arr and i!=0:
                return True
        return False
        