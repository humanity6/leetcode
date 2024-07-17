class Solution:
    def containsDuplicate(self, nums) -> bool:
        mydict = {}
        for i in nums:
            if i in mydict:
                return True
            else:
                mydict[i] = 1
        return False

# test cases
x = Solution()
print(x.containsDuplicate([1,2,3,1])) # True
print(x.containsDuplicate([1,2,3,4])) # False
print(x.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True
print(x.containsDuplicate([1,2,3,4,5,6,7,8,9,10])) # False
print(x.containsDuplicate([1,1,1,1,1,1,1,1,1,1])) # True