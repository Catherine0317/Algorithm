class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        
        if len(nums) <= 1:
            return nums[l]
        
        if nums[r] > nums[l]:
            return nums[l]
        
        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                l = mid + 1
            elif nums[r] > nums[mid]:
                r = mid 
            else:
                r -= 1
        return nums[l]
