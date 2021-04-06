class Solution{
    public:
    int removeuplicates(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) {
            return n;
        }

        int slow = 2, fast = 2;
        while (fast < n)
        {
            if(num[slow-2] != num[fast]) {
                nums[slow] = nums[fast];
                ++slow;
            }
            ++fast;
        }
        return slow;
    }
}