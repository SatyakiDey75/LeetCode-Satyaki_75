class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        d={')':'(','}':'{',']':'['}
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stk.append(i)
            elif i==')' or i=='}' or i==']':
                if len(stk)>0 and stk[-1]==d[i]:
                    stk.pop()
                else:
                    return False
        return stk==[]