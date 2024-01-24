from typing import Optional
from TreeNode import TreeNode

# Pseudo-Palindromic Paths in a Binary Tree
# Given a binary tree where node values are digits from 1 to 9, a path in the tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

# constraints and notes
# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 9


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode], cnt = 0) -> int:
        if not root: return 0
        cnt ^= 1 << (root.val - 1)
        if root.left is None and root.right is None:
            return 1 if cnt & (cnt - 1) == 0 else 0
        return self.pseudoPalindromicPaths(root.left, cnt) + self.pseudoPalindromicPaths(root.right, cnt)
