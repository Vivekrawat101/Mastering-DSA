# 🧠 Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates **in-place** such that each element appears only once.
# Return the new length and modify the array in-place.
# 
# Example:
# Input: nums = [1,1,2]
# Output: 2, nums becomes [1,2,_]
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
