# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/12 0:20
# @FileName : 155-最小栈.py
# @SoftWare : PyCharm

"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    push(x) —— 将元素 x 推入栈中。
    pop() —— 删除栈顶的元素。
    top() —— 获取栈顶元素。
    getMin() —— 检索栈中的最小元素。
思路：
    数据栈 + 辅助最小栈 (元素个数相同)
设计一个数据结构，使得每个元素 a 与其相应的最小值 m 时刻保持一一对应。因此我们可以使用一个辅助栈，与元素栈同步插入与删除，
用于存储与每个元素对应的最小值。
    - 当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；
    - 当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；
    - 在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中。  <<<<---------------------
"""

import math


class MinStack:
    """ 最小栈 """

    def __init__(self, min_val=math.inf):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [min_val]

    def push(self, val):
        """ push """
        self.stack.append(val)
        # TODO: 核心思想，在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        """ pop """
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        """ top """
        return self.stack[-1]

    def get_min(self):
        """ 最小值，常数时间复杂度 """
        return self.min_stack[-1]
