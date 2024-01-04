int smallestRepunitDivByK(int k) {
    int r=0;
    for (int l=1;l<=k;l++) {
        r=(r*10+1)%k;
        if (r==0)
            return l;
    }
    return -1;
}