
class Solution:
    def search(self, nums: [int], target: int) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        if n == 1:
            return nums[0] == target
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False


    def __init__(self):
        status = self.search([7,8,9,10,1,2,3,4,5,6],11)
        print(status)


if __name__ == "__main__":
    solution = Solution()

