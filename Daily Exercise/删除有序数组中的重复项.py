class Solution:
    def removeDuplicates(self, nums:[int]) -> int:
        length = len(nums)

        if length == 1:
            return 1

        slow, fast = 1, 1

        while(fast < length):
            if(nums[fast] != nums[fast-1]):
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        print(nums)            
        return slow

    def __init__(self):
       slow =  self.removeDuplicates([1,1,2,3,4,5,6,6,6,7,7,8,8,8,8,8,9])
       print(slow)


if __name__ == "__main__":
    solution = Solution()
