class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tgt_sum={}

        for index,num in enumerate(nums):
            if target-num in tgt_sum:
                return [tgt_sum[target-num],index]
            tgt_sum[num]=index
        