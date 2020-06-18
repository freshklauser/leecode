# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/14 17:00
# @FileName : missing_number.py
# @SoftWare : PyCharm

"""
题目：268.缺失数字
    给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
扩展：
    序列范围 start, end 中的 (end-start)个数，找出start到end中没有出现的数字
"""


def missing_number(nums, start=0):
    n = len(nums)
    nums.extend(list(range(start, n + start + 1)))
    res = 0
    for item in nums:
        res ^= item
    return res


def missing_number_hash(nums):
    n = len(nums)
    nums_map = {}
    for num in nums:
        nums_map[num] = 1
    res = [val for val in range(n + 1) if val not in nums_map][0]
    return res


def missing_number_index_xor(nums):
    """
    将索引与对应数值做异或，初始值为n
    由于索引只到 n-1， 没有出现n, 需要拿n做初始值
    TIPS: 如果数字不是从0开始，则应该考虑上一个方法
    """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing


if __name__ == '__main__':
    nums = [9, 3, 2, 8, 7, 5, 4, 1]
    res = missing_number(nums, start=1)
    nums_index = [0, 3, 2, 8, 7, 5, 4, 1]
    res_index = missing_number_index_xor(nums_index)
    print(res, res_index)

    nums = [0, 3, 2, 8, 7, 5, 4, 1]
    res = missing_number_hash(nums)
    print(res)
