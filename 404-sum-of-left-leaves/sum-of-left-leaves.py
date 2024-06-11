# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def rec(root,sum,flag):
            if not root:
                return sum
            if (not root.left and not root.right):
                if flag=='l':
                    sum+=root.val
                return sum
            sum=rec(root.left,sum,'l')+rec(root.right,sum,'r')
            return sum
        sum=rec(root,0,'r')
        return sum