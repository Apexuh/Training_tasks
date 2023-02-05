# #Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
#
#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
#
# ===============================
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, val1 in enumerate(nums):
#             r = target - val1
#             if r in nums and nums.index(r) != i:
#                 return i, nums.index(r)




# =================================================
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1 = [2,4,3]
l2 = [5,6,4]

l1 = int(''.join(list(map(str, l1[::-1]))))
l2 = int(''.join(list(map(str, l2[::-1]))))
l3 = list(map(int,str(l1 + l2)))[::-1]
print(l3)