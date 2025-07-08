arr = [1, 2, 3]
total = 0

for i in range(0, len(arr), 2):
    for j in range(i, len(arr)):
        total += sum(arr[i:j+1])

print(total)
