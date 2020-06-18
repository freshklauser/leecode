# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/14 11:55
# @FileName : letter_combination.py
# @SoftWare : PyCharm

"""
题目：17.电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

import itertools


class Solution:
    def letterCombinations(self, digits):
        res = []
        digits_map = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz')}
        for i, digit in enumerate(digits):
            if i == 0:
                res = digits_map[digit]
            else:
                tmp = []
                letters = digits_map[digit]
                for j in itertools.product(res, letters):
                    tmp.append(''.join(j))
                res = tmp
        return res


if __name__ == '__main__':
    digits = "253"
    ress = Solution().letterCombinations(digits)
    print(ress)
