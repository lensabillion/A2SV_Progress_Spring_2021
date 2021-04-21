# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        store = []
        s = ""
        ans = 0
        def dfs(root,s,store):
            if root:
                s += str(root.val)
            if root.left:
                dfs(root.left,s,store)
            if root.right:
                dfs(root.right,s,store)
            if not root.left and not root.right:
                store.append(s)
        dfs(root,s,store)
        for num in store:
            ans += int(num)
        return ans
        
        
        
