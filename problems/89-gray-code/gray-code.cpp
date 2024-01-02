class Solution {
public:
    vector<int> grayCode(int n) {
        long long len = pow(2, n);
        vector<int> arr;
        for (int i = 0; i < len; i++) {
            arr.push_back(i ^ (i >> 1));
        }
        return arr;
    }
};