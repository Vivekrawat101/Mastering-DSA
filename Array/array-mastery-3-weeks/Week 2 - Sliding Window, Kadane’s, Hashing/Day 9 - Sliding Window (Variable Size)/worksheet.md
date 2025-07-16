# 📘 Day 9 - Sliding Window (Variable Size)

## ✅ Topics
- Variable size sliding window
- Shrink-expand patterns for sum-based conditions

---

## 🧠 Concept Notes
Sliding window of variable size is useful when:
- The size of the window depends on a constraint (like sum or product)
- You want to minimize or maximize the size dynamically

### Common Logic:
Use two pointers `start` and `end` to maintain the window, expand `end`, and shrink `start` when constraints are violated.

---

## 🧪 Dry Run Tasks
Try dry-running these manually:
- `[2, 1, 5, 2, 3, 2]`, target = 7 → What's the smallest window with sum >= 7?
- `[1, 2, 1, 0, 1]`, k = 4 → What’s the longest window with sum <= 4?

---

## 💻 Code Practice Links
- [Smallest Subarray with Sum >= K – LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [Longest Subarray with Sum <= K – GFG](https://www.geeksforgeeks.org/longest-sub-array-sum-k/)
- [Longest Subarray with Sum = K – LC Premium/GFG](https://www.geeksforgeeks.org/longest-sub-array-sum-k/)

---

## 🧠 Goal
Master shrinking and expanding window techniques.
