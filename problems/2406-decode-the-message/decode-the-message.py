class Solution(object):
    def decodeMessage(self, key, message):
        d={" ":" "}
        ch="a"
        for i in key:
            if i not in d:
                d[i]=ch
                ch=chr(ord(ch)+1)
        return "".join(d[i] for i in message)