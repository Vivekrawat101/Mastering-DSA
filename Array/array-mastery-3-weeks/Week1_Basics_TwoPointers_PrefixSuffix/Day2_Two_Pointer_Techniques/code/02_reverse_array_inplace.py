# Problem: Reverse array using two pointers.
#
# Input: [1, 2, 3]
# Output: [3, 2, 1]


def reverse_array(arr):
    
    n = len(arr)
    i = 0
    j = n-1
    
    
    while i < (n//2):   #i<j : standard condition but this also works fine :)

        arr[i], arr[j] = arr[j], arr[i]
        
        i+=1
        j-=1
    
    return arr
        

print(reverse_array([1,2,3,4]))           
