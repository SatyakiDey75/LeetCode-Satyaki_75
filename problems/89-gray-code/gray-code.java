class Solution {
    public List<Integer> grayCode(int n) {
        int len = (int) Math.pow(2, n);
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            arr.add(i ^ (i >> 1));
        }
        
        return arr;
    }
}