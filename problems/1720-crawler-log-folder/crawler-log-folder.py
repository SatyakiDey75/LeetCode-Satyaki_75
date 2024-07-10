class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l=[]
        for i in logs:
            if i!="../" and i!="./":
                l.append(i)
            elif i=="../":
                l=l[:-1]
        return len(l)
        # count_1 = logs.count("../")
        # count_2 = logs.count("./")
        # count_3 = len(logs) - count_1 - count_2

        # if count_3 > count_1:
        #     return count_3 - count_1
        # return 0