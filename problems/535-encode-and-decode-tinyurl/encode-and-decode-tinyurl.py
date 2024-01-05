class Codec:

    char=string.ascii_letters+"0123456789"
    ctu={}
    utc={}
    def encode(self, lu):
        while lu not in self.utc:
            c=''.join(random.choice(self.char) for i in range (6))
            if c not in self.ctu:
                self.ctu[c]=lu
                self.utc[lu]=c
        return "http://tinyurl.com/"+self.utc[lu]

    def decode(self, su):
        return self.ctu[su[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))