# Problem: Compute prefix sum array.
# Input: [1, 2, 3]
# Output: [1, 3, 6]

def prefix_sum_array(arr):
    
    ctr = arr[0]
    n = len(arr)
    
    for i in range(1, n):
        
        ctr = ctr + arr[i] 
        arr[i] = ctr
    
    return arr



print(prefix_sum_array([1,2,3,4,5]))