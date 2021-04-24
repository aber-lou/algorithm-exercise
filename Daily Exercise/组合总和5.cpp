class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target+1,0);
        dp[0] = 1;
        for (int i = 1; i  <= target; i++) {
            for(auto a :nums) {
                dp[i] += dp[i-a];
            }
        }
        return dp.back();
    }
};