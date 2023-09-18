# Difficulty: Easy

class Solution:
    def removeDuplicates(self,nums):
        if len(nums) == 0:
            return 0
        i = 0
        j = 1 
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(nums))