class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result=[]
        req=''
        final=0
        for digit in digits:
            req+=str(digit)
            final=int(req)+1
        result=[int(num) for num in str(final)]
        return result
        