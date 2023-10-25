class Solution:
    def sortedSquares(self, nums):
        temp = []
        x = 0
        y = len(nums) - 1
        while x <= y:
            if abs(nums[x]) > abs(nums[y]):
                temp.insert(0, nums[x] * nums[x])
                x += 1
            else:
                temp.insert(0, nums[y] * nums[y])
                y -= 1
        return temp


s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))