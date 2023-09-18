# Difficulty: Easy

class Solution:
    def isValid(self, s: str):
        if len(s) % 2 != 0:
            return False
        stack = []
        map =  {"(":")", "[":"]", "{":"}"}
        
        for i in s:
            if i in  map.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                
                open_brac = stack.pop()

                if i != map[open_brac]:
                    return False
        return stack == []

s = Solution()
print(s.isValid("()"))
print(s.isValid("(()[]{}"))