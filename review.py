# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/7 22:58
# @FileName : review.py
# @SoftWare : PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.prev = float('-inf')

    def isValidBST(self, root):
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False

        if root.val <= self.prev:
            return False
        self.prev = root.val

        return self.isValidBST(root.right)