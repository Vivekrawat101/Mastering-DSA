"""
🟢 Valid Pair Exists (Two Pointer)

Problem:
Given a sorted array and a target, return True if any two distinct numbers add up to the target.

Input: [1,2,3,4,6], target = 5
Output: True  # (1,4) or (2,3)
"""

# Write your implementation here

def solution(arr, k):
    
    l=0
    r=len(arr)-1
    
    while(l<r):
        
        if arr[l]+ arr[r] > k:
            r-=1
            
        elif arr[l]+arr[r] < k:
            l+=1
        
        else:
            return True
    
    return False
 
print(solution([1,2,3,4,6], 5))