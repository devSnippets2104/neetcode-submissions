class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res="".join(map(str,digits))
        result=int(res)+1
        return list(map(int,str(result)))