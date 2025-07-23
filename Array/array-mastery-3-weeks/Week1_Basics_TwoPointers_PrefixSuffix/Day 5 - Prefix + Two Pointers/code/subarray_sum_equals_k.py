"""
Subarray Sum Equals K

Problem:
Count the number of continuous subarrays whose sum equals to `k`.

Input: nums = [1,1,1], k = 2
Output: 2  # Subarrays: [1,1] from index 0-1 and 1-2
"""

# Write your implementation here



def hashing_solution(arr,k):
    
    prefix_count = {0: 1}
    current_sum = 0
    count = 0
    
    for num in arr:
        
        current_sum += num
        
        if current_sum-k in prefix_count:
            
            count += prefix_count[current_sum-k]
        
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
    
    return count

print(hashing_solution([1, 2, 1, 2],3))