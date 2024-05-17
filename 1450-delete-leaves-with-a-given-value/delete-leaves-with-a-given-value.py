# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def rem(root):        
          if root==None or root.left==None and root.right==None:
            return 
          
          rem(root.left)and rem(root.right)
          if(root.left!=None):
            if root.left.val==target and root.left.left==None and root.left.right==None:
              root.left=None
          if root.right!=None:
            if root.right.val==target and root.right.left==None and root.right.right==None:
              root.right=None
          rem(root.left)
          rem(root.right)
        rem(root)
        rem(root)
        rem(root)
        if root!=None and root.left==None and root.right==None and root.val==target:
          return 
        return root
