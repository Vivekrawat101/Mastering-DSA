"""
🟢 Count Subarrays with Even Sum

Problem:
Count how many subarrays have an even total sum.

Input: [1,2,3,4]
Output: 4  # [1,2,3], [2], [3,4], [4]
"""

# Write your implementation here
def solution(arr):
    
    curr_sum = 0
    left = 0
    count = 0
    
    for right in range(0, len(arr)):
        
        curr_sum+=arr[right]
        
        if curr_sum%2!=0:
            
            curr_sum-=arr[left]
            left+=1
        
        count+=1    
    
    return count


print(solution([2,4,6]))    