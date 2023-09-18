# Difficulty: Easy

class Solution:
    def judgeCircle(self, moves):
        map1 = {
            "R" : 0,
            "L" : 0,
            "U": 0,
            "D": 0,
        }
        for i in moves:
            if i in map1:
                map1[i] += 1
        if map1['U'] == map1['D'] and map1['L'] == map1['R']:
            return True
        else:
            return False
        
    
s = Solution()
print(s.judgeCircle("UD"))
print(s.judgeCircle("LL"))
