class Solution(object):
    def decodeMessage(self, key, message):
        alp=list("abcdefghijklmnopqrstuvwxyz")
        mat= list(OrderedDict.fromkeys(list((key.replace(" ","")))))
        s=""
        for i in message:
            if i==" ":
                s+=i
            else:
                s+=alp[mat.index(i)]
        return s