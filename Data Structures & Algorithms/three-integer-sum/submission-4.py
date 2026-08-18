class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size=len(nums)
        result=[]
        summ=0
        for k in range(size-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i=k+1
            j=size -1

            while i < j :
                summ=nums[k]+nums[i]+nums[j]

                if summ == 0:
                    result.append([nums[k],nums[i],nums[j]])
                    i+=1
                    j-=1

                    while i < j and nums[i]==nums[i-1]:
                        i+=1
                    while i < j and nums[j] == nums [j+1]:
                        j-=1
                elif summ > 0:
                    j-=1
                else:
                    i+=1
        return result


        