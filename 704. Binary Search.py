# Difficulty: Easy

# recursion

class Solution:
    def search(self, nums, target):
        def binarysearch(low,high):
            if high>=low:
                mid = (low+high)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binarysearch(low,mid-1)
                else:
                    return binarysearch(mid+1,high)
            else:
                return -1
        return binarysearch(0,len(nums)-1)
    
# iterative
class Solution1:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while high>= low:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return -1
    

nums = [-1,0,3,5,9,12]
target = 9


s = Solution()
print(s.search(nums, target))

s = Solution1()
print(s.search(nums, target))
