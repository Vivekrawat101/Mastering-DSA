arr = [3, 7, 1, 9]

max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max:", max_val)
print("Min:", min_val)
