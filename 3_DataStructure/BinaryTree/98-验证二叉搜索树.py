# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/5 14:08
# @FileName : 98-验证二叉搜索树.py
# @SoftWare : PyCharm

"""验证二叉搜索树
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
Example 1:

        2
       / \
      1   3

    Input: [2,1,3]
    Output: true
思路：中序遍历，保存 prevalue 左比较
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.pre_val = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        # 中序遍历Step-1: 递归左子树
        if not self.isValidBST(root.left):
            return False

        # 中序遍历Step-2: 节点数据操作 （当前节点值>前一个结点值才True）
        if root.val <= self.pre_val:
            return False
        self.pre_val = root.val

        # 中序遍历Step-3: 遍历右子树
        return self.isValidBST(root.right)
