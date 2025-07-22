"""
🟢 Subarray Sum Equals K

Problem:
Count the number of continuous subarrays whose sum equals to `k`.

Input: nums = [1,1,1], k = 2
Output: 2  # Subarrays: [1,1] from index 0-1 and 1-2
"""

# Write your implementation here

def solution(nums,k):
    left = 0
    curr_sum = 0
    count = 0
    
    for right in range(len(nums)):
        curr_sum += nums[right]
        
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        
        if curr_sum == k:
            count += 1
    
    return count

print(solution([1, 2, 1, 2, 1], 3))
    