class Solution(object):
    def singleNonDuplicate(self, nums):
        return Counter(nums).most_common()[-1][0]