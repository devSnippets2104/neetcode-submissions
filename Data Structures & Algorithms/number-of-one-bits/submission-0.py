class Solution:
    def hammingWeight(self, n: int) -> int:
        count=quotient=0

        while n > 0:
            remainder = n %2
            if remainder ==1: count+=1
            quotient=(quotient*10)+remainder
            n//=2
        return count

        