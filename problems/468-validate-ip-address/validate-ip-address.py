def ipv4(s):
    f=0
    l=s.split('.')
    for i in l:
        if not i.isnumeric() or int(i)<0 or int(i)>=256 or str(int(i))!=i:
            f=1
    return f==0 and len(l)==4

def ipv6(s):
    f=0
    l=s.split(':')
    fa=[chr(i) for i in range(103,123)]
    for i in l:
        if i.isalnum():
            f=f-1 if any(j in i.lower() for j in fa) else f
        if len(i)<5 and (i.isalnum() or i.isnumeric()) and len(i)>=1:
            f+=1
    return f==8 and len(l)==8

class Solution(object):
    def validIPAddress(self, queryIP):
        if ipv4(queryIP):
            return "IPv4"
        if ipv6(queryIP):
            return "IPv6"
        return "Neither"
        