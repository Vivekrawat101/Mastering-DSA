# 📘 Day 3: Two Pointers with Conditions

## ✅ Topics
- Two Pointers with Conditional Logic
- In-place Modifications
- Smart Merging Techniques

---

## 🧠 Concept Notes

### 1. Two Pointers with Conditions
Used when you need to filter, compare, or rearrange elements based on rules, while maintaining array structure.

### 2. In-place Operations
You do not create a new array. You overwrite valid elements at the front and ignore the rest. Do not use `del`, `remove`, or `append`.

### 3. Merging Arrays In-Place
Start from the back of the array to avoid overwriting existing values. Work right-to-left using available space at the end.

---

## ❓ Conceptual Thinking Questions

- What does "in-place" actually mean?
- If I skip a value and don’t count it in the final length, is it deleted?
- Should I use `len(nums)` or maintain a custom counter?
- Is `0` a placeholder or part of logic in merge problems?
- Why must we preserve order in "Move Zeroes" but not always in "Remove Element"?

---

## 🧪 Conceptual Coding Questions

| Difficulty | Problem |
|------------|---------|
| Easy       | Filter only even numbers in-place and return new length |
| Easy       | Remove all negative numbers from array in-place |
| Medium     | From a sorted array, remove all duplicates such that each element appears at most twice (LC-style) |

(See `conceptual/` folder for these problems)

---

## 🧪 Dry Run Tasks

1. Dry run “Remove Duplicates” on `[1,1,2,2,3]`
2. Dry run “Move Zeroes” on `[0,1,0,3,12]`
3. Dry run “Merge Arrays” on `nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]`

---

## 💻 Code Practice Links

1. Remove Duplicates: [Leetcode #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
2. Move Zeroes: [Leetcode #283](https://leetcode.com/problems/move-zeroes/)
3. Merge Sorted Arrays: [Leetcode #88](https://leetcode.com/problems/merge-sorted-array/)

---

## 📈 Goal
Master conditional two-pointer logic that includes skipping, overwriting, or merging without using extra space.
