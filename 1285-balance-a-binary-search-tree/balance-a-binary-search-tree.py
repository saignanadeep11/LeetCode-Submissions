# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def trav(root):
            if not root:
                return 
            trav(root.left)
            arr.append(root.val)
            trav(root.right)
        trav(root)
        n=len(arr)
        # print(arr)
        
        def ins(l,r):
            if l>r:
                return None
            m=(l+r)//2

            root=TreeNode(arr[m])
            root.left=ins(l,m-1)
            root.right=ins(m+1,r)
            return root
        root=ins(0,n-1)

        # for i in 
        return root