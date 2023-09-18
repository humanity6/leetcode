# Difficulty: Medium


class Solution:
    def getAverages(self, nums, k: int):
        ele = (k*2)+1
        
        length = len(nums)
        average = [-1]*length

        if length < ele:
            return average
        
        prefixSum = [0] * (length + 1)
        for i in range(length):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        for i in range(k, length - k):
            average[i] = (prefixSum[i + k + 1] - prefixSum[i - k]) // ele
        
        return average
    
s = Solution()
print(s.getAverages([1,3,2,6,-1,4,1,8,2], 2))