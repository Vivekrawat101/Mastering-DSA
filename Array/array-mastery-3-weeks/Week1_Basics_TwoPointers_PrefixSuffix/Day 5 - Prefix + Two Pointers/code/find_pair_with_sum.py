"""
🟢 Find Pair with Given Sum (Two Pointers)

Problem:
Given a sorted array and a target, return True if a pair exists with that sum.

Input: [1,2,3,4,6], target = 7
Output: True  # Pairs: (1,6) or (3,4)
"""


def two_pointer_pair_sum(arr,k):

    l,r = 0, len(arr)-1
    
    
    while l < r:
        
        current = arr[l] + arr[r]
        
        if current == k:
            return True
    
        elif current < k:
            l += 1

        else:
            r -= 1
    
    return False
            
arr = [1,2,3,4,6] 
k = 7

print(two_pointer_pair_sum(arr,k))




def hash_pair_sum(arr, k):
    
    s = set()
    

    for num in arr:
        
        if k-num in s:
            
            return True
        
        if num not in s:
            
            s.add(num)
            
    return False          


print(hash_pair_sum(arr, k))
