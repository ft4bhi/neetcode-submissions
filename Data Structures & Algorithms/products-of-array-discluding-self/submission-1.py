class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1]*len(nums)

        left = 1
        for i in range(len(nums)):
            r[i]=left
            left*=nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            r[i]*=right
            right*=nums[i]
        
        return r