""" Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3 """

from typing import List


class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePath(self, root: TreeNode) -> List[str]:

        def dfs(root, path):

            if not root.left and not root.right:
                path.append(path)
                return

            if root.left:
                dfs(root.left, path + '->' + str(root.left.val))

            if root.right:
                dfs(root.right, path + '->' + str(root.right.val))

        paths = []
        if not root:
            return paths

        dfs(root, str(root.val))

        return paths
