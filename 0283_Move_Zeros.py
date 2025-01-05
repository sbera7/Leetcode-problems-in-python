class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter += 1
                continue
            if nums[i - counter] == 0:
                temp = nums[i - counter]
                nums[i - counter] = nums[i]
                nums[i] = temp
