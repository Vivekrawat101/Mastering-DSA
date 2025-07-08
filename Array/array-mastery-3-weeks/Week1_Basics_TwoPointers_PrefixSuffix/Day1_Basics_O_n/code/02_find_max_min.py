# Problem: Find max and min in the array.
# Input: [3, 7, 1, 9]
# Output: Max = 9, Min = 1



def find_min_max(arr):
    
    min = float('inf')
    max = float('-inf')
    n  = len(arr)
    for i in range(0, n, 1):
        
        if arr[i] > max:
            max = arr[i]
            
        if arr[i] < min:
            min = arr[i]
            
    return min, max


min_val, max_val = find_min_max([3, 5, 1, 4, 2])
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")