# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/21 21:26
# @FileName : 面试题59-滑动窗口的最大值.py
# @SoftWare : PyCharm

"""
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

slide_window:
for i in range(0, len(nums) - k + 1):
    pass

思路： 要求O(n)复杂度   单调双端队列
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        if not nums:
            return result
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i + k]))
        return result


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    obj = Solution()
    res = obj.maxSlidingWindow(nums, k)
    print(res)
