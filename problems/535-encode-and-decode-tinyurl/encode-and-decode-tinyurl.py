class Codec:
    def encode(self, lu):
        return lu


    def decode(self, su):
        return self.encode(su)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))