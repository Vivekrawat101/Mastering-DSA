"""
Move Zeroes to End (In-place)
-----------------------------
Given an integer array nums, move all 0's to the end while maintaining the 
relative order of the non-zero elements. Do this in-place.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Link: https://leetcode.com/problems/move-zeroes/
"""

def trailing_zeros(arr):
    
    n = len(arr)
    zind = 0
    for i in range(0,n):
        
        
        if arr[i] != 0:
            arr[zind],arr[i] = arr[i],arr[zind]
            zind+=1
        
    return arr


arr = [0,1,0,3,12]
print(trailing_zeros(arr))