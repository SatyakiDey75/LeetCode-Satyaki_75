int diagonalSum(int** mat, int matSize, int* matColSize) {
    int s=0;
    for (int i=0;i<matSize;i++)
        for (int j=0;j<matSize;j++)
            if (i==j || i+j==matSize-1)
                s+=mat[i][j];
    return s;
}