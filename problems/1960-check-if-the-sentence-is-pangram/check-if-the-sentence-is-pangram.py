class Solution(object):
    def checkIfPangram(self, sentence):
        return "abcdefghijklmnopqrstuvwxyz" == "".join(sorted(list(set(sorted("".join(sentence.split()))))))

        