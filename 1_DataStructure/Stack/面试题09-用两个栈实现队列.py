# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/21 20:57
# @FileName : 面试题09-用两个栈实现队列.py
# @SoftWare : PyCharm

"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数
和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
    输入：
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出：[null,null,3,-1]

思路：
    入队入到stack1
    出队从stack2出，Stack2为空时，将stack1倒入stack2，这样可以保证队列顺序

    删除：
        主栈和辅助栈都为空
            返回 -1
        辅助栈为空：
            将主栈元素移动至辅助栈
        辅助账不为空：
            直接返回辅助栈栈顶元素
"""


class CQueue:
    def __init__(self):
        self.main_stack = []
        self.extra_stack = []

    def appendTail(self, value):
        self.main_stack.append(value)

    def deleteHead(self):
        if not self.main_stack and not self.extra_stack:
            return -1
        elif not self.extra_stack:
            # 辅助栈为空，则将主栈元素移动至辅助账，否则直接弹出辅助栈元素
            while self.main_stack:
                self.extra_stack.append(self.main_stack.pop())
        return self.extra_stack.pop()
