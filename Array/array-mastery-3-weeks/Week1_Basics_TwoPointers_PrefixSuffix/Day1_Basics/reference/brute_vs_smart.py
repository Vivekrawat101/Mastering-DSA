# Brute force vs prefix sum for subarray sum
def brute_force_sum(arr, l, r):
    return sum(arr[l:r+1])

def prefix_sum_sum(prefix, l, r):
    return prefix[r] - (prefix[l-1] if l > 0 else 0)
