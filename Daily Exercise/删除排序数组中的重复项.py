class Solution:
    def removeDuplicates(self, nums:[int]) -> int:
        def solve(k):
            u = 0
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            print(nums[0:u])
            return u
        
        return solve(2)


    def __init__(self):
      a = self.removeDuplicates([1,1,1,1,1,1,2,2,2,2,2,2,3])
      print(a)


if __name__ == "__main__":
    s = Solution()

