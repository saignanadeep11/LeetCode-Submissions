# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans={}
        self.l=0
        self.r=0
        ret=[]
        def dfs(root,col,row ):
            if not root:
                return 
            self.l=min(self.l,col)
            self.r=max(self.r,col)
            if root:
                #TEst
                if not ans.get(col):
                    ans[col]=[]
                
                ans[col].append((row,root.val))
            dfs(root.left,col-1,row+1)
            dfs(root.right,col+1,row+1)
        dfs(root,0,0)
        for i in range(self.l,self.r+1):
            ans[i].sort()
            if(ans.get(i)):
                # ans[i].sort()
                ret.append([t[1] for t in ans[i]])
        # print(ret)
        # print(ans)
        return ret