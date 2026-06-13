class Solution:
    def isValid(self, s: str) -> bool:
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack=[]
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in pairs:
                if stack and pairs[char]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0