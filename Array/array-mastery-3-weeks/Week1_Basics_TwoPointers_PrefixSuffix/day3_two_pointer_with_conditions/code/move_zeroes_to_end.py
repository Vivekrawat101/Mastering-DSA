# ⚡ Move Zeroes to End (In-place)
# Given an integer array nums, move all 0's to the end while maintaining the relative order of the non-zero elements.
# Do this in-place without making a copy.
# 
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
def move_zeroes(nums):
    z = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[z] = nums[z], nums[i]
            z += 1
