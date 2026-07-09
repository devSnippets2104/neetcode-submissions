class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        size=len(numbers)
        seen=set()
        i=0
        j=size-1
        summ=0
        while i < j:
            summ=numbers[i]+numbers[j]
            if summ == target:
                return [i+1,j+1]
                i+=1
                j-=1
            elif summ < target:
                i+=1
            else:
                j-=1
        return res
        
        