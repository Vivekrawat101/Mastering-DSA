"""
 Min Subarray Length With Sum ≥ K

Problem:
Find the minimal length of a contiguous subarray of which the sum ≥ k.

Input: [2,3,1,2,4,3], k = 7
Output: 2  # Subarray: [4,3]
"""

# Write your implementation here


def solution(arr, k):
    
    min_len = float('inf')
    curr_sum = 0
    left = 0
    
    for right in range(0, len(arr)):
        curr_sum += arr[right]
    
    
        while curr_sum>=k:
            min_len = min(min_len, (right-left) +1)
            curr_sum-=arr[left]
            left+=1
    
    return min_len if min_len != float('inf') else 0

print(solution([2,3,1,2,4,3],7))