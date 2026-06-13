class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        feed_value={}
        for i,num in enumerate(nums):
            if target-num in feed_value:
                return [feed_value[target-num],i]
            
            feed_value[num]=i

            
        