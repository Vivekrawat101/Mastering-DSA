arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Brute-force
max_sum = float('-inf')
for i in range(len(arr)):
    for j in range(i, len(arr)):
        max_sum = max(max_sum, sum(arr[i:j+1]))
print("Brute:", max_sum)

# Kadane’s Algorithm
max_sum = curr = arr[0]
for num in arr[1:]:
    curr = max(num, curr + num)
    max_sum = max(max_sum, curr)
print("Kadane:", max_sum)
