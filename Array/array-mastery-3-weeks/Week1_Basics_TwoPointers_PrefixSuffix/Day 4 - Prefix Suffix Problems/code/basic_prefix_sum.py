"""
🧠  Basic Prefix Sum

Problem:
Build a prefix sum array for a given list and answer multiple range sum queries in O(1).

Example:
Input: arr = [2, 4, 1, 3, 7], queries = [(1,3), (0,2)]
Output: [8, 7]

https://leetcode.com/problems/range-sum-query-immutable/description/
"""

def range_query(arr, queries):
    
    result = []
    
    for idx in range(1, len(arr)):
        arr[idx] = arr[idx-1] + arr[idx]
    
    for item in queries:
        start,end = item
        
        if start != 0:
            result.append(arr[end] - arr[start-1])
        else:
            result.append(arr[end])    
    
    return result
    
        
arr =  [2, 4, 1, 3, 7]
queries = [(1,3), (0,2)]

print(range_query(arr, queries))

