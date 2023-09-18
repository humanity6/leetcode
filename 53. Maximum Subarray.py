class Solution:
    def maxSubArray(self, nums):
        pass

print("start")
def partition(array):
    if len(array) <= 1:
        return array
    else:
        
        mid = int(len(array)/2)
        print(f"right = {array[:mid]} --- left = {array[mid:]}")
        # right
        right = partition(array[:mid])
        # left 
        left = partition(array[mid:])
        print(sum(array))
        return sum(array)
    


nums = [-2,1,-3,4,-1,2,1,-5,4]
partition(nums)