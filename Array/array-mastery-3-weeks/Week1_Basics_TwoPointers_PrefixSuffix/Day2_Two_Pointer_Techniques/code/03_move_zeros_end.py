# Problem: Move all zeroes to the end of the array in-place.
#
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


def brute_trailing_zeros(arr):
    
    n = len(arr)
    z = 0
    i = 0
    
    while i < n:
        
        if arr[i] == 0:
            z = i 
            for j in range(i+1, n, 1):
                if arr[j]!= 0:
                    arr[z] = arr[j]
                    arr[j] = 0
                    break
                 
        i+=1
    return arr

def smart_trailing_zeros(arr):
    
    """
    Moves all zeroes to the end of the array in-place while maintaining the order of non-zero elements.
    
    This is an optimized version using a 'trap and swap' technique:
    - It traps the first zero and waits to find a non-zero
    - Swaps the trapped zero with the next non-zero
    - Continues scanning from the swapped position
    
    Args:
        arr (List[int]): Input list with integers.

    Returns:
        List[int]: Modified list with zeroes at the end.
    """
    
    
    n = len(arr)
    i = 0
    z = 0
    zflag = 0
    
    while i < n:
        
        if arr[i] == 0 and zflag == 0:
            
            z = i
            zflag = 1
        
        elif arr[i] != 0 and zflag == 1:
            arr[z],arr[i] = arr[i],arr[z]
            zflag = 0
            i = z
            

        #third case will be continuous zeros ... no need
        i+=1        
    
    return arr


print(smart_trailing_zeros([1,3,2,0,0,0,9,0,5,2]))
#print(brute_trailing_zeros([1,3,2,0,0,0,9,0,5,2]))