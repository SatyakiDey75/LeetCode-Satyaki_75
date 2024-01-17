// import math
class Solution {
    public int[] constructRectangle(int area) {
        int j=(int)Math.sqrt(area);
        while (area%j!=0)
            j-=1;
        int a[]={area/j,j};
        return a;
    }
}