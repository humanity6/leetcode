class Solution:
    def twoSum(self, numbers, target):
        hashmap = {}
        for index, num in enumerate(numbers, 1):
            second = target - num
            if second in hashmap and hashmap[second] != index:
                return [hashmap[second], index]
            hashmap[num] = index