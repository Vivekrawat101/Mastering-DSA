arr = [1, 10]
min_index = 0
max_diff = 0

for j in range(1, len(arr)):
    if arr[j] > arr[min_index]:
        max_diff = max(max_diff, j - min_index)
    if arr[j] < arr[min_index]:
        min_index = j

print(max_diff)
