# Difficulty: Easy

class Solution:
    def twoSum(self, nums, target: int):
        map = {}
        for i,v in enumerate(nums):
            if target-v in map:
                return [map[target-v],i]
            else:
                map[v] = i

nums = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums, target))