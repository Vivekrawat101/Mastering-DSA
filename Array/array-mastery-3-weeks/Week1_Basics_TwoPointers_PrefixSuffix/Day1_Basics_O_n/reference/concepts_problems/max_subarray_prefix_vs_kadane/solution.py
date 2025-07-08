arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Kadane’s
max_sum = curr = arr[0]
for num in arr[1:]:
    curr = max(num, curr + num)
    max_sum = max(max_sum, curr)
print("Kadane:", max_sum)

# Prefix sum
prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

min_prefix = 0
best = prefix[0]
for i in range(len(arr)):
    best = max(best, prefix[i] - min_prefix)
    min_prefix = min(min_prefix, prefix[i])

print("Prefix Sum:", best)
