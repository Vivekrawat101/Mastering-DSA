# Problem: Find max subarray sum using brute and optimized approach.
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


def brute_max_subarray_sum(arr, k):
    
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


def smart_max_subarray_sum(arr,k):
    
    # calculate length of arr
    n = len(arr)
    
    #initialize start and end index for subarray
    s=e=0

    #initialize sum
    m_sum = 0
    w_sum = 0
    #compute sum for 1st subarray
    for i in range(0, k):
        w_sum = w_sum + arr[i]
    
    m_sum = w_sum    
    #reinitialize end index for next window
    e = k
    
    #iterate till n-1 for computing max subarray sum
    while e<n:
        w_sum = w_sum-arr[s]+arr[e]
        m_sum = max(m_sum, w_sum)
        s+=1
        e+=1
    
    return m_sum



print(smart_max_subarray_sum([4, 2, 1, 7, 8, 1, 2, 8], 3))
print(brute_max_subarray_sum([-3, -1, -7, 0, -2], 1))