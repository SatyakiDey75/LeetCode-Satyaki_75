int rev(int x, int y) {
    long s=0;
    while (x>0) {
        s=(s*10)+(x%10);
        x=(int)x/10;
    }
    if (s>INT_MAX || s<INT_MIN)
        return 0;
    return s*y;
}

int reverse(int x){
    if (x>0 && x<INT_MAX)
        return rev(x,1);
    else if (x<0 && -x<INT_MAX)
        return rev(-x,-1);
    else
        return 0;
}