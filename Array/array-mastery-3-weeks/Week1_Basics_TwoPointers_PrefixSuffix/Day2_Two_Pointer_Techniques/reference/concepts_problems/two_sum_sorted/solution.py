arr = [1, 2, 4, 4]
target = 8
i, j = 0, len(arr) - 1
while i < j:
    if arr[i] + arr[j] == target:
        print(True)
        break
    elif arr[i] + arr[j] < target:
        i += 1
    else:
        j -= 1
else:
    print(False)
