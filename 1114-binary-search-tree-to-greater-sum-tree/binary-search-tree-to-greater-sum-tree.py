# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum=0
        def trav(root,sum):
            if not root:   
                return sum
            sum=trav(root.right,sum)
            sum+=root.val
            # print(root.val,sum)
            root.val=sum
            sum=trav(root.left,sum)
            # print(sum)
            return sum
        trav(root,sum)
        # trav(root.left,sum)
        return root