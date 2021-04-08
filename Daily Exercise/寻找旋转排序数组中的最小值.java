class Solution {
    public int finddMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            if(nums[left] < nums[right]) {
                return nums[left];
            }

            int mid = left + ((right - left) >> 1);
            if(nums[left] <= nums[mid]) {
                left = mid + 1;
            } else if(nums[left] > nums[mid]) {
                right = mid;
            }
        }
        return -1;    
    }
}