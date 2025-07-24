"""
 Max Subarray Sum ≤ K

Problem:
Find the length of the longest subarray with sum ≤ k.

Input: [1,2,1,0,1], k = 4
Output: 4  # Subarray: [1,2,1,0]
"""

# Write your implementation here

def solution(arr,k):
    
    curr_sum = 0
    max_len = float('-inf')
    left = 0
    
    
    for right in range(0, len(arr)):
        
        curr_sum += arr[right]

        
        while curr_sum > k:
            
            curr_sum -= arr[left]
            left+=1

        max_len = max(max_len, (right-left) +1)            
    
    return 0 if max_len == float('-inf') else max_len

print(solution([1,2,1,0,1],4))
                
        
        
        
