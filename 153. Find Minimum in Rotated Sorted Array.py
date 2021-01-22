class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        l = 0
        r = len(nums) - 1
        
        if len(nums) <= 1:
            return nums[l]
        
        if nums[r] > nums[l]:
            return nums[l]
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid+1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]
