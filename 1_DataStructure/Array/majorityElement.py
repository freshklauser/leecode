# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/13 18:12
# @FileName : majorityElement.py
# @SoftWare : PyCharm

"""
题目：
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1:
    输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
    输出: 2

思路：
1）摩尔投票法： 正负相抵
票数和： 由于众数出现的次数超过数组长度的一半；若记 众数 的票数为 +1，非众数 的票数为 −1，则一定有所有数字的 票数和 >0。
票数正负抵消：设数组 nums 中的众数为 x ，数组长度为 nnn 。
    若 nums 的前 a个数字的 票数和 =0，则 数组后 (n−a) 个数字的 票数和一定仍 >0（即后 (n−a)个数字的 众数仍为 x ）。
2）算法流程:
    初始化： 票数统计 votes=0， 众数 x；
    循环抵消： 遍历数组 nums 中的每个数字 num ；
        当 票数 votes等于 000 ，则假设 当前数字 num为 众数 x；
        当 num=x时，票数 votes 自增 1 ；否则，票数 votes自减 1 。
    返回值： 返回 众数 x 即可。
"""

from collections import Counter
print([item for item in dir(Counter) if not item.startswith('_')])


class Solution:
    def majorityElement_hash(self, nums):
        if len(nums) == 1:
            return nums[0]
        half = len(nums) / 2
        res = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        return res[0][0] if res[0][1] > half else None

    def majorityElement_vote(self, nums):
        """ 摩尔投票法:核心理念为 正负抵消 """
        vote = 0
        for num in nums:
            if vote == 0:
                target = num
            if num == target:
                vote += 1
            else:
                vote -= 1
        return target


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 2, 2, 2, 5, 4, 2, 5, 2, 5]
    res = Solution().majorityElement_hash(nums)
    res1 = Solution().majorityElement_vote(nums)
    print(res, res1)
