"""
🟢 Count Subarrays with Even Sum

Problem:
Count how many subarrays have an even total sum.

Input: [1,2,3,4]
Output: 4  # [1,2,3], [2], [1,2,3,4], [4]
"""

# Write your implementation here
def solution(arr):
    
    from collections import defaultdict

    count = defaultdict(int)
    count[0] = 1  # Empty prefix sum is considered even
    prefix_sum = 0
    result = 0

    for num in arr:
        prefix_sum += num
        parity = prefix_sum % 2

        # Add the number of subarrays ending here with same parity
        result += count[parity]

        # Update the count for this parity
        count[parity] += 1
        print(count[parity])
    return result

print(solution([1,2,3,4]))    