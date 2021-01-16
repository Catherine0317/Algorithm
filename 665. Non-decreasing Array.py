class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        nums1 = nums[:]
        nums2 = nums[:]
         
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums1[i] = nums[i+1]
                nums2[i+1] = nums[i]
                break 
        return nums1 == sorted(nums1) or nums2 == sorted(nums2)
