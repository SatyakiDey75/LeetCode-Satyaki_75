class Solution {
    public double myPow(double x, int n) {
        long nn=0;
        if (x==1)
            return 1;
        if (x==-1)
        {
            if (n%2==0)
                return 1;
            if (n%2!=0)
                return -1;
        }
        if(n<0)
            nn=(long)n *-1;
        else
            nn=(long)n;
        int p=1;
        while(nn>1 && nn%2==0 && p<=100000)
        {
            p=p*2;	
            nn=nn/2;
        }
        System.out.println(p+" "+nn);

        double ans=1,ans2=1;
        if (n>=0)
        {
            for(long i=1;i<=nn;i++)
                ans*=x;
            for(long i=1;i<=p;i++)
                ans2*=ans;
        }
        else
        {
            for(long i=1;i<=nn;i++)
                ans/=x;
            for(long i=1;i<=p;i++)
                ans2*=ans;
        }
        return ans2;
    }
}