int rev(long x, int y) {
    long s=0;
    while (x>0) {
        s=(s*10)+(x%10);
        x=(long)x/10;
    }
    if (s>INT_MAX || s<INT_MIN)
        return 0;
    return s*y;
}

int reverse(long x){
    if (x>0)
        return rev(x,1);
    else
        return rev(-x,-1);
}