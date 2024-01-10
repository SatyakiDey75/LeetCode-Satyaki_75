class Solution(object):
    def decrypt(self, code, k):
        c=[0]*len(code)
        if k==0:
            return c
        for i in range (len(code)):
            s,n,b=0,i+1,k
            if k<0:
                n=i-1
                b*=(-1)
            for j in range (b):
                print(s,code[n%len(code)],n%len(code))
                s+=code[n%len(code)]
                if k<0:
                    n-=1
                else:    
                    n+=1
            c[i]=s

        return c