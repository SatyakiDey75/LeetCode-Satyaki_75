def rec(t):
    for i in range (0,len(t)):
        if t[i]=="+":
            t[i-2]=(int(t[i-2])+int(t[i-1]))
            return t[:i-1]+t[i+1:]
        elif t[i]=="-":
            t[i-2]=(int(t[i-2])-int(t[i-1]))
            return t[:i-1]+t[i+1:]
        elif t[i]=="*":
            t[i-2]=(int(t[i-2])*int(t[i-1]))
            return t[:i-1]+t[i+1:]
        elif t[i]=="/":
            t[i-2]=(int(int(t[i-2])/int(t[i-1])))
            return t[:i-1]+t[i+1:]
class Solution:
    def evalRPN(self, t: List[str]) -> int:
        while len(t)>1:
            t=rec(t)
        return int(t[0])