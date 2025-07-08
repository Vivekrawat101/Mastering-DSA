arr = [1, 2, 3]
suffix = [0] * len(arr)
suffix[-1] = arr[-1]

for i in range(len(arr) - 2, -1, -1):
    suffix[i] = arr[i] + suffix[i + 1]

print("Suffix Array:", suffix)
