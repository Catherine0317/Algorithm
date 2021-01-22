class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = 0 
        r = len(nums) - 1
        
        if nums == []:
            return [-1,-1]
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                i = mid - 1
                j = mid + 1
                while i >= 0 and nums[i] == target:
                    i -= 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                return [i+1,j-1]
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return [-1,-1]
