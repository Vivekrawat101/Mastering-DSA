"""
🧠  Suffix Max Array

Problem:
Construct a suffix max array and count elements greater than all elements to their right.

Example:
Input: [4, 3, 2, 5, 1]
Output: 2  # 5 and 1
"""


def suffix_max(arr):

    suffix = arr[:]
    right_max = suffix[-1]
    
    for idx in range(len(suffix)-2,-1,-1):    
        
        if suffix[idx] < right_max:
            suffix[idx] = right_max
        
        else:
            right_max = suffix[idx]
        
    
    return suffix
    
arr=[4, 3, 2, 5, 1]
suffix_arr = suffix_max(arr)
print(suffix_arr)
n = len(arr)
max_num = arr[-1]
count = 0

    
for idx in range(n-2, -1, -1):

    if arr[idx] > max_num:
        
        count += 1
        max_num = arr[idx]
        
    
print(count)
     