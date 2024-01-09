class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] ans = new int[n];
        
        if (k == 0) {
            return ans;
        }

        for (int i = 0; i < n; i++) {
            int j = 0;
            int sum = 0;
            int count = k;

            if (k > 0) {
                j = i + 1;
                while (count-- > 0) {
                    sum += code[j % n];
                    j++;
                }
            } else {
                if (i == 0) {
                    j = n - 1;
                } else {
                    j = i - 1;
                }
                while (count++ < 0) {
                    sum += code[j];
                    if (j == 0) {
                        j = n - 1;
                    } else {
                        j--;
                    }
                }
            }
            ans[i] = sum;
        }

        return ans;
    }
}