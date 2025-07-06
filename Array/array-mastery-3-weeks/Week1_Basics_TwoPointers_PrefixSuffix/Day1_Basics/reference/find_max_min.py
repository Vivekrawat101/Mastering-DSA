def find_max_min(arr):
    max_val = float('-inf')
    min_val = float('inf')
    for num in arr:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
    return max_val, min_val
