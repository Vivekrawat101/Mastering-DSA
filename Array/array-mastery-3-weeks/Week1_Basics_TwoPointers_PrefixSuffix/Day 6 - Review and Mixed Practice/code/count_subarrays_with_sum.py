"""
Count Subarrays With Fixed Sum

Problem:
Count how many subarrays sum exactly to `k`.

Input: nums = [1,2,3], k = 3
Output: 2  # Subarrays: [1,2], [3]
"""

# Write your implementation here

def solution(arr,k):
    
    s = {0:1}
    curr_sum = 0
    count = 0
    
    for i in arr:
        
        curr_sum+=i
        
        if curr_sum - k in s:
            
            count += s[curr_sum-k]
            
        s[curr_sum] = s.get(curr_sum, 0) + 1

    return count

print(solution([1,1,1,2,3],3))
