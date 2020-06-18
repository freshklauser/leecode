# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/17 6:37
# @FileName : 最长公共前缀.py
# @SoftWare : PyCharm


"""
14. 最长公共前缀
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。
示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"
"""


class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            shorter = min(len(prefix), len(strs[i]))
            if shorter == 0:
                return ''
            index = 0
            while index < shorter and prefix[index] == strs[i][index]:
                index += 1
            prefix = prefix[:index]
        return prefix


if __name__ == '__main__':
    s = ['aa', 'a']
    res = Solution().longestCommonPrefix(s)
    print(res)
