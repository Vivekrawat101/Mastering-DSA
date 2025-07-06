def build_suffix_max(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        suffix[i] = max(arr[i], suffix[i+1])
    return suffix
