class Solution(object):
    def integerReplacement(self, n):
        c=0
        while n!=1:
            if n%2==0:
                n/=2
            else:
                if ((n-1)/2)%2==0:
                    n-=1
                elif n==3:
                    c+=2
                    break
                elif ((n+1)/2)%2==0:
                    n+=1
            c+=1
        return c
        