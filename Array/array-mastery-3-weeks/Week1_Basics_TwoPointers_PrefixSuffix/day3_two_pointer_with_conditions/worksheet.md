# 📘 Day 3: Two Pointer with Conditions

## ✅ Topics Covered
- In-place updates using two pointers
- Remove duplicates in sorted arrays
- Move zeroes to end while keeping order
- Merge sorted arrays efficiently

---

## 🧠 Concept Notes

Two Pointer (with conditions):
- You maintain two indices: one that reads, one that writes/swaps.
- Powerful for **sorted arrays**, **in-place modification**, and **real-time cleanup**.

Common tricks:
- Fast and slow pointer (read-write pattern)
- Zero trap + swap technique
- Backward merging to avoid shifting

---

## 🧪 Dry Run Tasks

1. Dry run `remove_duplicates([1,1,2,2,3])` — track `i` and `j`.
2. Manually trace `move_zeroes([0,1,0,3,12])` — mark swaps.
3. Merge `nums1=[1,3,5,0,0,0]`, `nums2=[2,4,6]` and walk backwards.

---

## 💻 Code Practice Links

- [Remove Duplicates from Sorted Array – Leetcode #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [Move Zeroes – Leetcode #283](https://leetcode.com/problems/move-zeroes/)
- [Merge Sorted Array – Leetcode #88](https://leetcode.com/problems/merge-sorted-array/)

---

## 📈 Goal

Be able to:
- Use two pointers with overwrite logic
- Optimize for **in-place** operations (O(1) space)
- Write bug-free, efficient code for cleanup tasks in arrays
