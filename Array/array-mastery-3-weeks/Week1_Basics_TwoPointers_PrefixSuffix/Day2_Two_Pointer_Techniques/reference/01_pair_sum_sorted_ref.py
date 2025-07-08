arr = [1, 2, 3, 4, 6]
target = 6

i, j = 0, len(arr) - 1
found = False

while i < j:
    s = arr[i] + arr[j]
    if s == target:
        found = True
        break
    elif s < target:
        i += 1
    else:
        j -= 1

print(found)
