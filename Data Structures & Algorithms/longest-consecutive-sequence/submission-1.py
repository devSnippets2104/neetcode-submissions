class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        max_len=0

        for num in seen:
            if num -1 not in seen:
                length=1
                current = num
                while current+1 in seen:
                    length+=1
                    current+=1
                max_len=max(max_len,length)
        return max_len

