s = "racecar"
left, right = 0, len(s) - 1

while left < right:
    if s[left] != s[right]:
        print(False)
        break
    left += 1
    right -= 1
else:
    print(True)
