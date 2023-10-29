class Solution:
    def intToRoman(self, num: int) -> str:
        def intToRoman1(num: str) -> str:
            l=['','I','II',"III","IV","V","VI","VII","VIII","IX","X"]
            x=int(num)
            return l[x]
        def intToRoman2(j: str) -> str:
            o=''
            s=str(j)
            x=int(j)
            if j[0]=="0":
                x=0
            if x>=90:
                o=o+"XC"
            elif x>=50:
                o=o+"L"+"X"*(int(s[0])-5)
            elif x>=40:
                o=o+"XL"
            elif x<40:
                o=o+"X"*int(s[0])
            c=intToRoman1((s[1:]))
            return str(o)+str(c)
        def intToRoman3(j: str) -> str:
            o=''
            s=str(j)
            x=int(j)
            if j[0]==0:
                x=0
            if x>=900:
                o=o+"CM"
            elif x>=500:
                o=o+"D"+"C"*(int(s[0])-5)
            elif x>=400:
                o=o+"CD"
            elif x<400:
                o=o+"C"*int(s[0])
            c=intToRoman2((s[1:]))
            return str(o)+str(c)
        def intToRoman4(x: str) -> str:
            o=''
            s=str(x)
            i=int(x)
            o=o+"M"*int(s[0])
            c=intToRoman3((s[1:]))
            return str(o)+str(c)
        
        x=num
        o=''
        s=str(x)
        if len(s)>3:
            o=intToRoman4(s)
        elif len(s)>2:
            o=intToRoman3(s)
        elif len(s)>1:
            o=intToRoman2(s)      
        else:
            o=intToRoman1(s)
        return o
