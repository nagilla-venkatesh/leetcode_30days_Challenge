"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example :

Input: root = [1,null,3,2,4,null,5,6]
Output: 3
"""

from collections import deque

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        q = deque()
        q.append(root)
        level = 0

        while q:
            length = len(q)

            for _ in range(length):
                current = q.popleft()

                for child in current.childern:
                    q.append(child)

            level += 1
        return level

