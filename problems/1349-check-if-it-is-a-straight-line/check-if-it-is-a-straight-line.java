class Solution {
    public boolean checkStraightLine(int[][] c) {
        if (c.length==2)
            return true;
        int a=-(c[1][1]-c[0][1]), b=(c[1][0]-c[0][0]), c1=-a*c[0][0]-b*c[0][1];
        for (int i=2;i<c.length;i++)
            if ((a*c[i][0]+b*c[i][1]+c1)!=0)
                return false;
        return true;
    }
}