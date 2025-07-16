# 📘 Day 8: Sliding Window (Fixed Size)

## ✅ Topics
- Sliding window for **fixed-size subarrays**
- Maintain a window of `k` elements and update as you slide
- Optimize problems involving "every k-size chunk"

---

## 🧠 Concept Notes

- A **fixed window** means the subarray size remains constant.
- Start by computing the sum of the first window.
- Slide the window by removing the first element and adding the next.
- Time complexity improves from O(n\*k) to O(n).

---

## 🧪 Dry Run Tasks

1. Slide a window of size 3 over `[1, 2, 3, 4, 5]`. What are the sums?
2. Max sum subarray of size 2 in `[2, 1, 5, 1, 3, 2]`?
3. Average of all subarrays of size 4 in `[1, 3, 2, 6, -1, 4, 1, 8, 2]`?

---

## 💻 Conceptual Coding Questions

### 🟢 Easy 1: Max Sum Subarray of Size K
Filename: `code/max_sum_subarray_k.py`

---

### 🟢 Easy 2: Average of All Subarrays of Size K
Filename: `code/average_subarrays_k.py`

---

### 🟡 Medium: Max Sum of Contiguous Subarray Size K (Handle Negatives)
Filename: `code/max_sum_k_with_negatives.py`

---

## 📈 Goal
- Learn how to implement and **slide** a fixed-size window
- Reduce brute-force O(n\*k) to O(n)
- Build confidence for harder patterns (variable sliding next!)
