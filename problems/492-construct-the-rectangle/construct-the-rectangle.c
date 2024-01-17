/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
int* constructRectangle(int area, int* returnSize) {
    int j=sqrt(area);
    while(area%j!=0)
        j-=1;
    int* a=(int*)malloc(2*sizeof(int));
    a[0]=area/j;
    a[1]=j;
    *returnSize=2;
    return a;
}