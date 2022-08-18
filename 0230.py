# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    times=0
    ans=0
    def kthSmallest(self, root, k: int) -> int:
        self.times=0
        self.ans=0
        def zhongxu(root):
            if(root.left):
                zhongxu(root.left)
            self.times+=1
            if(self.times==k):
                self.ans= root.val
                return
            if(root.right):
                zhongxu(root.right)
        zhongxu(root)
        return self.ans
