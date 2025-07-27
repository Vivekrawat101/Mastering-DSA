"""
🟡 Count Subarrays with Sum in Range [L, R]

Problem:
Count how many subarrays have sum in the range [L, R].

Input: nums = [1,2,3], L = 3, R = 5
Output: 3  # [1,2], [2,3], [3]
"""

# Write your implementation here
def solution(arr, L, R):
    
    count = 0
    s = {0:1}
    curr_sum = 0
    
    for num in range(0, len(arr)):
        
        curr_sum += arr[num]
        
        for key in range(curr_sum-R, curr_sum-L +1) :
            
            if key in s:
                
                count += s[key]

        s[curr_sum] = s.get(curr_sum,0)+1
    return count

print(solution([1,2,3],3,5))
