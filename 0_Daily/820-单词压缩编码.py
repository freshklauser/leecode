# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-28 10:59:25
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-28 11:56:39

'''单词压缩编码
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
示例：
    输入: words = ["time", "me", "bell"]
    输出: 10
    说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
思路：
    cur_length = 0
    index_list = [0]
    for i in range(len(words)):
        cur_length += len(words[i] + 1)
        if words[i + 1] in words[i]:
            index = (cur_length - 1) - len(words[i + 1])
        else:
            index = cur_length
            cur_length += words[i + 1] + 1
        index_list.append(index)
'''


class Solution:
    def minimumLengthEncoding(self, words):
        total = set(words)
        for word in words:
            for k in range(1, len(word)):
                total.discard(word[k:])
        length = sum(len(word) + 1 for word in total)
        return length


if __name__ == '__main__':
    words = ["time", "me", "bell"]
    res = Solution().minimumLengthEncoding(words)
    print(res)
