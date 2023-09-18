# Difficulty: Easy

class Solution:
    def singleNumber(self, nums):
        mymap = {}
        for i in nums:
            if i in mymap:
                mymap[i] += 1
            else:
                mymap[i] = 1

        for key, value in mymap.items():
            if value == 1:
                return key

nums = [4,1,2,1,2]
s = Solution()
print(s.singleNumber(nums))