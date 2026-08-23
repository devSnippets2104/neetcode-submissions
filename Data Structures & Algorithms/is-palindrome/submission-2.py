class Solution:
    def is_alnum(self,char:str):
        return ('A' <= char <='Z') or ('a' <= char <= 'z') or ('0' <=char <= '9')
    def is_lower(self,char:str):
        if 'A' <= char <='Z':
            return chr(ord(char) + 32)
        return char
    def isPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1

        while start < end:
            while start < end and not self.is_alnum(s[start]):
                start+=1
            while start < end and not self.is_alnum(s[end]):
                end-=1
            
            if self.is_lower(s[start]) != self.is_lower(s[end]):
                return False

            start+=1
            end-=1
        return True

        