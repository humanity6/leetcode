class Solution:
    # IF IT WORKS IT WORKS
    def balancedStringSplit(self, s: str) -> int:
        mysum, balanced = 0,0
        for i in s:
            if mysum == 0:
                balanced += 1
            if i == "R":
                mysum += 1
            else:
                mysum -= 1
        return balanced

s = Solution()
print(s.balancedStringSplit("RLRRLLRLRL"))
print(s.balancedStringSplit("RLLLLRRRLR"))
print(s.balancedStringSplit("LLLLRRRR"))