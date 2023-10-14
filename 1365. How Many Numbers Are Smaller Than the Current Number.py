class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_array = sorted(nums)
        indices = []

        for num in nums:
            index = sorted_array.index(num)
            indices.append(index)

        return indices


s = Solution()

print(s.smallerNumbersThanCurrent([8,1,2,2,3]))