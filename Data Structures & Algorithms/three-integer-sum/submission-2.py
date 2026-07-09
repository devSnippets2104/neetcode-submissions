class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        summ=0
        result=[]
        for k in range(len(nums)-2):
            if k >0 and nums[k]==nums[k-1]:
                continue
            i=k+1
            j=len(nums)-1
            while i <j:
                summ=nums[k]+nums[i]+nums[j]
                if summ==0:
                    result.append([nums[i],nums[j],nums[k]])
                    i+=1
                    j-=1
                    while i < j and nums[i]==nums[i-1]:
                        i+=1
                    while i < j and nums[j]==nums[j+1]:
                        j-=1
                elif summ < 0:
                    i+=1
                else:
                    j-=1
        return result
                    

            
        