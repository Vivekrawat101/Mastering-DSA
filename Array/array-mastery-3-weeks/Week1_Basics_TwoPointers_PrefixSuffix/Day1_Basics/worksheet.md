# 📘 Day 1: Basics to Build Intuition (O(n))

Master the foundational techniques that help you avoid brute-force and think in O(n) for array problems.

---

## ✅ Topics to Learn

- [ ] Prefix Sum Basics  
- [ ] Suffix Array Basics  
- [ ] Finding Max/Min in an Array in O(n)  
- [ ] Brute Force vs Smart Code (Visual Examples)

---

## 🧠 Concept Notes

### 🔹 Prefix Sum
- Build a running total: `prefix[i] = prefix[i-1] + arr[i]`
- Useful for subarray sum queries: `sum(l, r) = prefix[r] - prefix[l-1]`

### 🔹 Suffix Array
- Build from right: `suffix[i] = max(arr[i], suffix[i+1])`
- Great for greedy and reverse logic problems

### 🔹 Max/Min in O(n)
- Use one pass with tracking variable:
  ```python
  max_val = float('-inf')
  for x in arr:
      if x > max_val:
          max_val = x
  ```

### 🔹 Brute vs Smart
- Brute: Nested loops, slow for large inputs
- Smart: Use precomputation (prefix), space-time tradeoffs

---

## 🧪 Dry Run Tasks

- [ ] Create prefix sum for `[1, 2, 3, 4, 5]`
- [ ] Create suffix max array for `[3, 1, 4, 2, 5]`
- [ ] Compare brute vs optimized for sum(l, r) queries
- [ ] Write Python code to find max/min in one pass

---

## 💻 Code Practice Links

### ✅ Prefix Sum Problems
- https://leetcode.com/problems/range-sum-query-immutable/
- https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/

### ✅ Max/Min in Array
- https://leetcode.com/problems/maximum-subarray/
- https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

---

## 📈 Goal for Day 1

- Understand how to compute and use prefix/suffix arrays
- Clearly see difference between brute-force vs optimized logic
- Be able to solve O(n) traversal-based array problems confidently
