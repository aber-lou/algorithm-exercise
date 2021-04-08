class Solution:
    def finddMin(self,nums:[]) -> int:
        
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def __init__(self):
        min = self.finddMin([8,9,10,2,5,6,7])
        print(min)


if __name__ == "__main__":
    solution = Solution()




    
