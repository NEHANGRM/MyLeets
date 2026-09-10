# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        self.ans=0
        def dfs(node):
            if not node:
                return 0,0
            left_sum,left_cnt=dfs(node.left)
            right_sum,right_cnt=dfs(node.right)
            tot_sum=left_sum+right_sum+node.val
            tot_cnt=left_cnt+right_cnt+1
            if tot_sum//tot_cnt == node.val:
                self.ans+=1
            return tot_sum,tot_cnt
        dfs(root)
        return self.ans