# Problem: Compute suffix sum array.
# Input: [1, 2, 3]
# Output: [6, 5, 3]


def suffix_sum_array(arr):
    
    n = len(arr)
    ctr = arr[n-1]
    
    for i in range(n-2, -1, -1):
        
        ctr = ctr + arr[i]
        
        arr[i] = ctr 
    
    return arr

print(suffix_sum_array([1,2,3,4,5]))