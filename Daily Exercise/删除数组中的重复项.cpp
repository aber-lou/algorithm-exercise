class Solution {
public:
    int removeDuplicates(vector<int> &nums) {

        int len = nums.size();
        if(len == 0 || len == 1) {
            return len;
        }
        int slow = 1, fast = 1;

        while (fast < n)
        {
            if (nums[fast] != nums[fast - 1]) {
                nums[slow] = nums[fast];
                slow += 1;
            }
            fast += 1;
        }
        return slow;

    }

}