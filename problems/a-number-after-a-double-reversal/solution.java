class Solution {
    public boolean isSameAfterReversals(int n) {
        int bkp=n,r=0,q=0;
        for (;n>0;n/=10)
            r=r*10+(n%10);
        for (;r>0;r/=10)
            q=q*10+(r%10);
        if (bkp==q)
            return true;
        else
            return false;
    }
}