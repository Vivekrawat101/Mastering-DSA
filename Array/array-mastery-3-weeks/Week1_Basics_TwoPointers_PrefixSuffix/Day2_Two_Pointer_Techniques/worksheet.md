# 📘 Day 2: Two Pointer Techniques (Left–Right Traversal)

Learn how to use two pointers effectively on arrays — especially sorted ones — to avoid brute force and improve to O(n).

---

## ✅ Topics to Learn

- [ ] Two Pointer for Pair Search (sorted array)
- [ ] Reverse Array using Two Pointers
- [ ] In-place Shifting (Move Zeros, Remove Duplicates)
- [ ] Real-world use cases (Container Problem, Palindrome Check)

---

## 🧠 Concept Notes

### 🔹 Two Pointers
- Use left and right index to eliminate nested loops
- Example: `while left < right:` — move based on condition

### 🔹 Pair Search in Sorted Array
- If `arr[i] + arr[j] > target` → decrease `j`
- If `arr[i] + arr[j] < target` → increase `i`

### 🔹 Reverse Array
- Swap `arr[left]` and `arr[right]`, then move both inward

### 🔹 In-Place Zero Movement
- Maintain a slow pointer to track position for non-zero elements

---

## 🧪 Dry Run Tasks

- [ ] Dry run two sum with `[1,2,3,4,6]` and target `6`
- [ ] Reverse `[10, 20, 30, 40]` using two pointers
- [ ] Move zeros in `[0,1,0,3,12]` in-place

---

## 💻 Code Practice Links

- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- https://leetcode.com/problems/reverse-string/
- https://leetcode.com/problems/move-zeroes/
- https://leetcode.com/problems/container-with-most-water/
- https://leetcode.com/problems/valid-palindrome/

---

## 📈 Goal for Day 2

- Use two pointers comfortably for array problems
- Write in-place clean code without extra space
- Spot where this pattern can replace nested loops
