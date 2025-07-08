arr = [1, 2, 3]
prefix = []
curr = 0

for num in arr:
    curr += num
    prefix.append(curr)

print("Prefix Sum:", prefix)
