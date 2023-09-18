# Difficulty: Medium

class Solution:
    def canJump(self, nums):
        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])
        return True

nums = [2,3,1,1,4]
s = Solution()
print(s.canJump(nums))