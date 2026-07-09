class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size=len(heights)
        max_value=0
        i=0
        j=size-1

        while i < j:
            area= (j-i) * min(heights[i],heights[j])
            max_value=max(max_value,area)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return max_value



        