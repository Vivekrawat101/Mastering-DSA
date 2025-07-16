"""
⚙️  Equal Prefix and Suffix Sum

Problem:
Count indices where prefix sum (0 to i) == suffix sum (i to n-1)

Example:
Input: [1, 2, 3, 3]
Output: 1  # At index 2
"""

def prefix_sum(arr):
    prefix_arr = arr[:]
    for idx in range(1, len(prefix_arr)):
        prefix_arr[idx] = prefix_arr[idx] + prefix_arr[idx-1]
    
    return prefix_arr


def suffix_sum(arr):
    suffix_arr = arr[:]
    for idx in range(len(suffix_arr)-2, -1, -1):    
        suffix_arr[idx] = suffix_arr[idx] + suffix_arr[idx+1] 
    
    return suffix_arr


arr = [1,2,3,3]

prefix_array = prefix_sum(arr)
suffix_array = suffix_sum(arr)

equal_sum_ctr = 0

for i,j in zip(prefix_array,suffix_array):
    
    if i == j:
        equal_sum_ctr+=1

print(equal_sum_ctr)



