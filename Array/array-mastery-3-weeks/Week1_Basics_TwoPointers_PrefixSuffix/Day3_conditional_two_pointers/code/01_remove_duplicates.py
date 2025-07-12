"""
Remove Duplicates from Sorted Array
-----------------------------------
Given an integer array sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
Return the number of unique elements.

Example:
Input: nums = [1,1,2]
Output: 2
nums becomes [1,2,_] (rest ignored)

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

def remove_duplicates(arr):
    
    n = len(arr)
    i = 1
    j = 1

    while j < n:
        
        if arr[j] != arr[j-1]:
                 
            arr[i] = arr[j]
            i+=1              
  
            
        j+=1

    return i


def leetcode_solve(arr):
    
    i = 0
    
    for j in range(1, len(arr)):
        
        if arr[j] != arr[i]:
            # if iter is not equals to slow pointer then distinct element is found 
            # keep it at next slow pointer index
            i += 1
            arr[i] = arr[j]
    
    return i+1
            
  
            
arr=[1,1,1,2,2,3,3,3,4,4,4,5]

# k = remove_duplicates(arr)
k = leetcode_solve(arr)
print(f'{k}, nums = {arr[:k]}')