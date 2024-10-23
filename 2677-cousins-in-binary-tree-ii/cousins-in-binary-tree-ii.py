# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lev=0
        que=deque()
        que.append(root)
        levsum=defaultdict(int)
        while(que):
            n=len(que)
            sum=0
            for _ in range(n):
                r=que.popleft()
                sum+=r.val
                if(r.left):
                    que.append(r.left)
                if(r.right):
                    que.append(r.right)
            levsum[lev]=sum
            lev+=1
        def dfs(root,lev):
            if not root:
                return 
            curSum=0
            if(root.left):
                curSum+=root.left.val
            if(root.right):
                curSum+=root.right.val
                root.right.val=levsum[lev+1]-curSum
            if root.left:
                root.left.val=levsum[lev+1]-curSum
            dfs(root.left,lev+1)
            dfs(root.right,lev+1)
        dfs(root,0)
        root.val=0
        return root