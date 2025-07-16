# 📘 Day 5: Prefix Sum + Two Pointers

## ✅ Topics
- Prefix Sum for range-based calculations
- Two Pointer search techniques
- Optimizing subarray queries with precomputed sums

---

## 🧠 Concept Notes

- **Prefix Sum + Two Pointer** is often used when you need to find **subarrays** that satisfy a condition based on their sum.
- Instead of checking all subarrays (O(n²)), prefix sums help compute subarray sums in O(1), and two pointers help **move efficiently**.

### Example Patterns:
- Find subarray with sum `k`
- Find count of subarrays within a range
- Minimum/maximum size subarray satisfying a sum condition

---

## 🧪 Dry Run Tasks

1. Dry run prefix sum on `[1, 2, 3, 4, 5]` → What is the sum from index 1 to 3?
2. Use two pointers on sorted `[1, 2, 3, 4, 6]` to find if any two numbers sum to 7.
3. Combine both on `[1, 1, 1, 2, 3]` to find subarrays summing to 3.

---

## 💻 Conceptual Coding Questions

### 🟢 Easy 1: Subarray Sum Equals K (Sliding Two Pointers)

Filename: `code/subarray_sum_equals_k.py`

---

### 🟢 Easy 2: Find Pair with Given Sum in Sorted Array (Two Pointers)

Filename: `code/find_pair_with_sum.py`

---

### 🟡 Medium: Min Subarray Length With Sum ≥ K (Two Pointers + Prefix)

Filename: `code/min_subarray_len_sum_k.py`

---

## 📈 Goal
- Learn how prefix sums can quickly answer range-sum queries.
- Combine them with two pointers to avoid brute force.
- Build intuition for “subarray sliding + sum checking”.
