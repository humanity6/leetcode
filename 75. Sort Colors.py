class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        ones = 0
        twos = 0
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                ones += 1
            else:
                twos += 1
        for i in range(zero):
            nums[i] = 0
        for i in range(ones):
            nums[zero + i] = 1
        for i in range(twos):
            nums[zero + ones + i] = 2     