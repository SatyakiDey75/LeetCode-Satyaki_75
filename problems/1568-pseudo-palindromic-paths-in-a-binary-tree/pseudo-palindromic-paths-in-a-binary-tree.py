# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root: Optional[TreeNode], path: int) -> None:
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                path^=1<<root.val
                if path & (path-1)==0:
                    ans+=1
                return
            dfs(root.left,path^1<<root.val)
            dfs(root.right,path^1<<root.val)
        dfs(root,0)
        return ans
            