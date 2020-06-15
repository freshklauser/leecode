# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/6/16 6:04
# @FileName : strStr_implement.py
# @SoftWare : PyCharm

"""
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串
出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
示例 1:
    输入: haystack = "hello", needle = "ll"
    输出: 2
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """ 滑动窗口 """
        if not needle:
            return 0
        longer = len(haystack)
        shorter = len(needle)
        first = -1
        for i in range(longer - shorter + 1):
            win = haystack[i:i + shorter]
            if win == needle:
                first = i
                break
        return first

    def strStr_cursor(self, haystack, needle):
        """
        双指针
        tips:
            外层结束while条件：haystack遍历到最后与needle等长子串仍不满足条件时索引不越界
        步骤：
            （1）移动haystack指针找起始匹配点
            （2）从起始匹配点开始移动双指针逐项匹配，记录匹配长度
            （4）匹配长度不等于needle长度，则将haystack指针回退到起始匹配点的下一个点作为新的起始匹配点
            同时将匹配长度和needle的指针置0
        """
        if not needle:
            return 0
        longer = len(haystack)
        shorter = len(needle)
        index_max = longer - shorter + 1
        cur_hay = 0
        while cur_hay < index_max:

            # 找匹配起点的index
            while cur_hay < index_max and haystack[cur_hay] != needle[0]:
                cur_hay += 1

            # 找到起点时索引为 cur_hay
            cur_nee = 0
            length = 0
            while cur_nee < shorter \
                    and cur_hay < longer \
                    and haystack[cur_hay] == needle[cur_nee]:
                cur_hay += 1
                cur_nee += 1
                length += 1

            if length == shorter:
                return cur_hay - length

            # backtrack, 从上一个起点的下一个点开始重新匹配
            cur_hay = cur_hay - length + 1

        return -1


if __name__ == '__main__':
    haystack = "hehhosdtihhe"
    needle = "hhe"
    res = Solution().strStr_cursor(haystack, needle)
    print(res)
