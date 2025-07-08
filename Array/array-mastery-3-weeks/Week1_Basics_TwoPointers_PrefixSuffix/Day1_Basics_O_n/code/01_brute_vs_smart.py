# Problem: Find max subarray sum using brute and optimized approach.
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


def max_subarray_sum(arr, k):
    
    n = len(arr)
    max_sum = float('-inf')
    temp_sum = 0
    i = 0
    
    while k+i <= n:
        
        temp_sum = 0
        
        for j in range (n - (k+i), n-i, 1):

            temp_sum = temp_sum + arr[j]
            
        if temp_sum > max_sum:
            max_sum = temp_sum
    
        i+= 1    
    return max_sum     


print(max_subarray_sum([-3, -1, -7, 0, -2], 1))