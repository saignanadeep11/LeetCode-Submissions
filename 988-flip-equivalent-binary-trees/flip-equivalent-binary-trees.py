# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root1,root2):
            
            if not root1 and not root2:
                return 
            elif(root1 and not root2)or (not root1 and root2):
                return 
            
            if(root1.left and root2.left)and(root1.right and root2.right):
                if(root1.left.val==root2.left.val)and(root1.right.val==root2.right.val):
                    pass
                elif(root1.left.val==root2.right.val)and(root1.right.val==root2.left.val):
                    # print(root1.val)
                    temp=root1.left
                    root1.left=root1.right
                    root1.right=temp
                
            elif(root1.left and root2.right):
                if(root1.left.val==root2.right.val):
                    temp=root1.left
                    root1.left=root1.right
                    root1.right=temp
            elif(root1.right and root2.left):
                if(root1.right.val==root2.left.val):
                    temp=root1.right
                    root1.right=root1.left
                    root1.left=temp
            
            dfs(root1.left,root2.left)
            dfs(root1.right,root2.right)
            
            return 
        def tran(root1,root2):
            # print(root1,root2)
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            # print(root1.val)
            return tran(root1.left,root2.left) and tran(root1.right,root2.right) and root1.val==root2.val
        dfs(root1,root2)
        k=tran(root1,root2)
        return k