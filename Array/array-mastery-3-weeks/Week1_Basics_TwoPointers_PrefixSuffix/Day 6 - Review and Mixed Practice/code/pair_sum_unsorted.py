"""
 Pair Sum Exists (Unsorted Array)

Problem:
Given an unsorted array and a target, return True if any pair sums to target.

Input: [5, 3, 1, 7], target = 8
Output: True  # Pairs: (5,3)
"""

# Write your implementation here
def sum_exists(arr, k):
    
    n = len(arr)
    s = set()

    for num in arr:
        
        if k-num in s:
            
            return True

        else:
            s.add(num)
            
    return False
    

print(sum_exists([5, 3, 1, 7],8))