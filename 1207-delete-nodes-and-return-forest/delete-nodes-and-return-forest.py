# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        l=None
        dic=defaultdict(TreeNode)
        def dfs(root,ans,l):
            # print(root,ans)
            if not root:
                return
            if root:
                root.left=dfs(root.left,ans,l)
                root.right=dfs(root.right,ans,l)
            if root.val in to_delete:
                dic[root.val]=None
                if root.left and root.left.val not in to_delete:
                    dic[root.left.val]=root.left
                if root.right and root.right.val not in to_delete:
                    dic[root.right.val]=root.right
                root=None
        
            return root
        dfs(root,ans,l)
        if root.val not in to_delete:
            dic[root.val]=root
        # print(dic)
        for i in dic:
            if dic[i]:
                ans.append(dic[i])
        # print(l,ans)
        return ans
