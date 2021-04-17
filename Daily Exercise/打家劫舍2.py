class Solution:
    def rob(self, nums:[int]) -> int:
        def robRange(start: int ,end : int) -> int:
            first = nums[start]
            second = max(first, nums[start + 1])
            for i in range(start + 2, end + 1):
                temp = second
                second = max(first + nums[i], second)
                first = temp
            return second

        length = len(nums)



        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(0, length - 2), robRange(1, length - 1))


    def __init__(self):
        sum = self.rob([1,3,2,4,1,1,8,1,5,1,0])
        print(sum)


if __name__ == "__main__":
    solution = Solution()
