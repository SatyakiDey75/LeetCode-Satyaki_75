int diagonalSum(int** mat, int matSize, int* matColSize) {
    int s=0,n=matSize;
    for (int i=0;i<n;i++){
        s+=mat[i][i];
        if (i!=n-1-i)
            s+=mat[i][n-1-i];
    }          
    return s;
}