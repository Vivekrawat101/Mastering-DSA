# Problem: Check if a pair exists with a target sum in sorted array.
#
# Input: [1, 2, 3, 4, 6], target = 6
# Output: True

def brute_pair_exists(arr,k):
    n = len(arr)    
    
    for i in range (0,n,1):

        item = arr[i]
        
        for j in range(i+1, n, 1):
            
            if arr[j] == k-item:
                
                return True  
    return False

def smart_pair_exists(arr, k):
    
    s = set()
    n = len(arr)
    for i in range(0, n, 1):
        
        if k-arr[i] in s:
            
            return True

        s.add(arr[i])
    
    return False
    




    
print(brute_pair_exists([1,3,3,1,1], 6))
print(smart_pair_exists([1,3,0,1,1], 6))


