class Solution {
    public int[] leftRightDifference(int[] nums) {
        int l[]=new int[nums.length];
        for (int i=0;i<nums.length;i++) {
            int ls=0,rs=0;
            for (int j=0;j<i;j++)   ls+=nums[j];
            for (int j=i+1;j<nums.length;j++)  rs+=nums[j];
            l[i]=(ls>rs)?ls-rs:rs-ls;
        }
        return l;
    }
}
