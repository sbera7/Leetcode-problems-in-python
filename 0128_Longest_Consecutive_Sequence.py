class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        nums.sort()
        max = 0  
        count = 0
        for index, n in enumerate(nums):
            if index == 0:
                continue
                
            if nums[index] - nums[index-1] == 1:
                count += 1
                if count > max:
                    max = count
            else:
                count = 0

        return max + 1 
