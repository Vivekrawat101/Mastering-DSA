"""
Merge Two Sorted Arrays (In-Place)
----------------------------------
Given two sorted arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
nums1 has a size equal to m + n, where the first m elements denote the elements to merge,
and the last n elements are set to 0 and should be ignored.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3
       nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

Link: https://leetcode.com/problems/merge-sorted-array/
"""


def merge_sorted_arrays(nums1, nums2, m, n):
       
       i = n-1
       j = m-1
       k = (n+m)-1
       
       while j >= 0:
              
              if nums2[j] > nums1[i]:
                     
                     nums1[k] = nums2[j]
                     j-=1

              else:
                     nums1[k] = nums1[i]
                     i-=1

              k-=1                  
       
       return nums1
       
       
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]       
m = 3
n = 3

print(merge_sorted_arrays(nums1, nums2, m, n))