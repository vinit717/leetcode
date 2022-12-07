# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans, stack = 0, deque([root])
        while stack:
            node = stack.pop()
            if not node: continue

            if   node.val <  low: stack.append(node.right)
            elif node.val > high: stack.append(node.left )
            else:
                ans+= node.val
                stack.append(node.left )
                stack.append(node.right)
                
        return ans