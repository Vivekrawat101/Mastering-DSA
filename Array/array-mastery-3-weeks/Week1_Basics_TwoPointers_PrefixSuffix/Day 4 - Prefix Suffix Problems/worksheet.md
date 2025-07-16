# 📘 Day 4: Prefix Suffix Problems

## ✅ Topics
- Advanced Prefix Sum
- Suffix Array Techniques
- Handling nested prefix conditions
- Subarray range logic

## 🧠 Concept Notes

Prefix/Suffix arrays are cumulative representations:
- `PrefixSum[i] = arr[0] + arr[1] + ... + arr[i]`
- `SuffixSum[i] = arr[i] + arr[i+1] + ... + arr[n-1]`

Use them when:
- You're asked about **range queries**.
- You want to convert **O(n^2) sum calculations** into **O(1) using pre-computed arrays**.
- You need to **track conditions in multiple directions (left-to-right and right-to-left)**.

Common Patterns:
- Prefix sums to calculate subarray sums in O(1).
- Suffix arrays to track right-side conditions.
- Often combined with hash maps for prefix frequency patterns.

---

## 🔍 Conceptual Thinking Questions

1. What does the prefix sum at index `i` tell us, and how can it be used for subarray sum calculations?
2. How is a suffix array different from a prefix sum array in usage?
3. When is combining prefix sum with hash map necessary in a problem?

---

## 💻 Conceptual Coding Questions

### 🧠 Easy 1 — `basic_prefix_sum.py`
> Build a prefix sum array for a given list and answer multiple range sum queries in O(1).

**Example**

Input: arr = [2, 4, 1, 3, 7], queries = [(1,3), (0,2)]
Output: [8, 7]

### 🧠 Easy 2 — `suffix_max_array.py`
> Construct a suffix max array where `suff[i] = max(arr[i:])` and use it to find count of elements which are greater than all elements to their right.

**Example**

Input: [4, 3, 2, 5, 1]
Output: 2 # Elements 5 and 1

### ⚙️ Medium — `equal_prefix_suffix_sum.py`
> Count number of indices where prefix sum (0 to i) = suffix sum (i to n-1).

**Example**

Input: [1, 2, 3, 3]
Output: 1 # At index 2, both sides = 6

---

## 🔗 Code Practice Links

- [Prefix Sum Range Query - Leetcode](https://leetcode.com/problems/range-sum-query-immutable/)
- [Count Elements With Greater Right - GFG](https://www.geeksforgeeks.org/count-elements-on-left-and-right-that-are-greater-than-current/)
- [Equal Prefix Suffix Sum - Practice](https://www.geeksforgeeks.org/find-the-index-where-the-sum-of-left-subarray-is-equal-to-the-sum-of-right-subarray/)

---

## 🧪 Dry Run Tasks

- Manually build prefix and suffix arrays on [3, 1, 4, 2, 5]
- Try queries like sum(1, 3) using prefix array
- Find index where prefix == suffix using manual table

---

## 📈 Goal
Master range-sum logic, prefix/suffix dual traversal, and nested cumulative strategies for arrays.
