# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def search(val,par,lev):
            if not par:
                return
            if par.left:
                if(par.left.val==val):
                    return [par.val,lev+1]
            if par.right:
                if(par.right.val==val):
                    return [par.val,lev+1]
            return search(val,par.left,lev+1)or search(val,par.right,lev+1)
        first=search(x,root,0)
        sec=search(y,root,0)
       
        if not first or not sec:
            return False
        if(first[0]!=sec[0] and first[1]==sec[1]):
            return True
        return False