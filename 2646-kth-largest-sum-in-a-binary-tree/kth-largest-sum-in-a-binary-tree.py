# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSum=defaultdict(int)
        def dfs(root,level):
            if not root:
                return
            levelSum[level]+=root.val
           
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        dfs(root,0)
        sums=list(levelSum.values())
        sums.sort(reverse=True)
        n=len(sums)
        if k>n :
            return -1
        return sums[k-1]