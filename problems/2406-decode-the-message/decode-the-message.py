class Solution(object):
    def decodeMessage(self, key, message):
        # alp=list("abcdefghijklmnopqrstuvwxyz")
        # mat= list(OrderedDict.fromkeys(list((key.replace(" ","")))))
        # s=""
        # for i in message:
        #     if i==" ":
        #         s+=i
        #     else:
        #         s+=alp[mat.index(i)]
        # return s
        # more optimised:
        dict_of_keys={" ":" "}
        char="a"
        for i in key:
            if i not in dict_of_keys:
                dict_of_keys[i]=char
                char=chr(ord(char)+1)
        return "".join(dict_of_keys[i] for i in message)