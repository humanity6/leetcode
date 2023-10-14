class Solution:
    def missingNumber(self, nums):
        miss = len(nums)
        for i in range(len(nums)):
            miss = miss ^ (i ^ nums[i])
        return miss

s = Solution()
print(s.missingNumber([0,1,3]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))