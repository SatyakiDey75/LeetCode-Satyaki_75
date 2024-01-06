class Solution(object):
    def decodeMessage(self, key, message):
        dict_of_keys={" ":" "}
        char="a"
        for i in key:
            if i not in dict_of_keys:
                dict_of_keys[i]=char
                char=chr(ord(char)+1)
        return "".join(dict_of_keys[i] for i in message)