class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        y = bin(n)[2:].rjust(32,"0")
        return int(y[::-1],2)